from flask import Flask, request, render_template, redirect, url_for, flash, send_file
import os
from .data_processing import extract_data_from_pdf
from .clustering import cluster_incidents
from .comparison import plot_bar_graph
from .custom import plot_custom_pie_chart
import pandas as pd
import urllib.request

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.secret_key = "your_secret_key"  
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

clustered_data = None
data = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    global clustered_data, data

    files = request.files.getlist("file")
    urls = request.form.get("urls")

    if not files and not urls:
        flash("No files or URLs provided.")
        return redirect(url_for("index"))

    all_incidents = []
    nature_counts = {}

    # Handle uploaded files
    for file in files:
        if file.filename != "":
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            file_nature_counts, file_incidents = extract_data_from_pdf(file_path)
            nature_counts.update(file_nature_counts)
            all_incidents.extend(file_incidents)

    # Handle URLs
    if urls:
        url_list = urls.split(",")
        for url in url_list:
            url = url.strip()
            try:
                # Download the PDF from the URL
                with urllib.request.urlopen(url) as response:
                    pdf_data = response.read()

                    file_name = url.split("/")[-1]
                    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

                    # Save the downloaded PDF in the 'uploads' folder
                    with open(pdf_path, 'wb') as f:
                        f.write(pdf_data)

                    # Extract data from the downloaded PDF
                    url_nature_counts, url_incidents = extract_data_from_pdf(pdf_path)
                    nature_counts.update(url_nature_counts)
                    all_incidents.extend(url_incidents)
                    
            except Exception as e:
                flash(f"Error downloading or processing the PDF from URL {url}: {str(e)}")
                continue

    data = pd.DataFrame(all_incidents, columns=["Date", "Incident Number", "Location", "Nature", "ORI"])
    data["Count"] = data["Nature"].map(nature_counts)

    data.dropna(subset=["Nature", "Count"], inplace=True)

    clustered_data = cluster_incidents(data)

    return redirect(url_for("visualization"))


@app.route("/visualization")
def visualization():
    return render_template("visualization.html")


@app.route("/graph/clustering")
def graph_clustering():
    global clustered_data

    if clustered_data is None:
        flash("No data available. Please upload a file first.")
        return redirect(url_for("index"))
    img = cluster_incidents(data, num_clusters=3)  # Pass the correct DataFrame

    if img is None:
        flash("There was an issue generating the clustering graph.")
        return redirect(url_for("index"))
    return send_file(img, mimetype='image/png')


@app.route("/graph/bar")
def graph_bar():
    global data
    if data is None:
        flash("No data available. Please upload a file first.")
        return redirect(url_for("index"))

    img = plot_bar_graph(data)

    if img is None:
        flash("There was an issue generating the bar chart.")
        return redirect(url_for("index"))

    return send_file(img, mimetype='image/png')


@app.route("/graph/custom")
def graph_custom():
    global data
    if data is None:
        flash("No data available. Please upload a file first.")
        return redirect(url_for("index"))

    img = plot_custom_pie_chart(data)

    if img is None:
        flash("There was an issue generating the custom graph.")
        return redirect(url_for("index"))

    return send_file(img, mimetype='image/png')


def create_app():
    return app
