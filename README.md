# cis6930fa24 -- Project 3 -- Template

Name: Sharvani Gouni

# Project Description 
This project enables users to upload one or more NormanPD-style incident PDFs and visualizes the data in an interactive web interface. The tool extracts key information from the uploaded PDFs and presents it in three distinct visualizations. The first visualization shows a clustering of records, helping to group similar incidents. The second visualization is a bar graph that compares different results from the data. The third visualization is a custom chart chosen to provide additional insights from the dataset. This interface makes it easy to explore and analyze the data collected from the Norman Police Department incident reports, helping users gain valuable insights quickly.

# How to install
pipenv install

## How to run
pipenv run python main.py

to run test cases : pipenv run python -m pytest

## Video

## Functions

#### data_processing.py 
extract_data_from_pdf: This function extracts incident data from a NormanPD-style PDF file and organizes it into two parts: a dictionary of incident types (Nature) and a list of incident details. It reads each page of the PDF and processes the text to extract relevant fields such as the incident time, number, location, nature, and origin. The function splits each line of text based on multiple spaces, identifies and skips irrelevant lines (like page numbers or report headers), and then stores the extracted data. It also counts how many times each "nature" (incident type) appears, which can be used for further analysis or visualization. The output includes two elements: a dictionary with counts of each incident type and a list of tuples containing the full incident details.

#### clustering.py 
cluster_incidents: This function clusters incident types ('Nature') based on their frequency and generates a scatter plot to visualize the clusters. It first counts how many times each incident type appears, then uses KMeans clustering to group them into specified clusters (default is 3). The function creates a scatter plot where the x-axis shows the incident types, the y-axis shows their counts, and colors represent the different clusters. The plot is saved in memory and returned as an image buffer.

#### comparison.py 
plot_bar_graph: This function generates a bar chart to visualize the frequency of different incident types ('Nature'). It first checks if the data contains a 'Nature' column, then counts the occurrences of each incident type. The bar chart is plotted with customized labels and colors. The plot is created in memory and returned as an image buffer for use in the application. The chart’s layout is adjusted to prevent overlapping elements, and the x-axis labels are rotated for better readability.

#### custom.py
plot_custom_pie_chart: This function creates a custom pie chart to visualize the distribution of incident types ('Nature'). It first checks if the data contains the necessary 'Nature' column, then counts the occurrences of each type. The function generates a color palette using seaborn and handles any errors by falling back to default colors. The pie chart is plotted with percentages displayed on each wedge and customized with a title. The chart is saved in memory and returned as an image buffer. The layout is adjusted to avoid overlaps, ensuring the pie chart remains circular.

#### app.py
index(): This function renders the main page of the application (the index page), where users can upload PDF files or provide URLs containing the incident data. It is the entry point of the app.

upload_file(): This function handles file uploads and URL submissions. It checks whether files or URLs are provided by the user. For uploaded files, it saves them to a specified directory and extracts incident data using the extract_data_from_pdf() function. If URLs are provided, it downloads the PDF, extracts the data, and updates the overall dataset. The function also processes the data into a pandas DataFrame, adding a 'Count' column, cleaning the data by dropping rows with missing values, and then performs clustering on the data using the cluster_incidents() function. After processing, it redirects to the visualization page.

visualization(): This function renders the visualization page where users can view different visualizations of the incident data. It is called after the data is uploaded and processed.

graph_clustering(): This function generates the clustering visualization. It calls the cluster_incidents() function to generate a clustering plot based on incident types ('Nature') and returns the plot as a PNG image for display in the browser.

graph_bar(): This function generates a bar chart comparing the frequency of incident types (from the 'Nature' column) using the plot_bar_graph() function. The bar chart is returned as a PNG image to be displayed in the browser.

graph_custom(): This function generates a custom pie chart visualization of incident distribution by type ('Nature') using the plot_custom_pie_chart() function. The pie chart is returned as a PNG image to be displayed in the browser.

create_app(): This function creates and returns the Flask app. It allows the app to be instantiated and used with different configurations if needed.

#### main.py
This code is used to initialize and run the Flask web application. The create_app() function from the src.app module is called to create the Flask app instance. The app.run() method is then used to start the Flask development server, making the application accessible on all available network interfaces (host="0.0.0.0") on port 5000. The debug=True argument enables debug mode, allowing for automatic code reloading and detailed error messages during development. This setup is typically used during development and testing before deploying the app in a production environment.


#### index.html
This HTML template provides a simple, user-friendly interface for uploading incident data via PDF files or URLs. The form includes fields for selecting multiple PDF files or entering URLs separated by commas. The layout is clean and responsive, featuring a header, styled input fields, and a large submit button. Feedback messages are displayed in a red box for errors or success. The design ensures ease of use with clear labels, a green button with a hover effect, and real-time notifications to guide users through the upload process.

#### visualization.html
This HTML template provides a user-friendly interface for viewing various data visualizations. It includes a header with the title "Visualization Options" and a central container with navigation links for users to view different types of graphs, such as clustering graphs, bar charts, and custom pie charts. Each link directs the user to the corresponding graph page. Flash messages are displayed to provide real-time feedback, such as errors or success notifications. The graphs are displayed dynamically within the page as images once they are generated, using the base64 encoding format. The design is modern and responsive, with smooth hover effects on the links and visually appealing graph display styles.

#### test_app.py 
client (pytest fixture): This function sets up a test client for the Flask app. It enables testing by setting app.testing = True to enable detailed error messages and using Flask's test_client() to simulate requests to the app. The fixture provides a client object that can be used to make HTTP requests and check the app’s responses during testing. The yield client statement returns the client for use in the test, and once the test is done, the client is automatically cleaned up.

test_index(client): This test function checks if the index route (/) of the application is working correctly. It sends a GET request to the root URL and asserts that the response has a status code of 200 (OK). It also verifies that the page contains the text "Upload PDF" to ensure the correct content is being rendered on the page.

test_visualization(client): This function tests the /visualization route of the app to ensure it returns the correct response. It sends a GET request to the /visualization URL and checks if the response status code is 200 (OK). It also verifies that the page contains the word Clustering,indicating that the correct content (for visualization) is being loaded and displayed.

#### test_comparison.py 
test_plot_bar_chart_valid_data: This test checks whether the plot_bar_chart function works correctly with valid data. A sample DataFrame is created with incident types under the "Nature" column. The function is called to generate a bar chart, and the test asserts that the returned object is a BytesIO object (since the image is returned in memory). It then reads the image data and ensures that it is not empty, confirming that the function successfully generates and returns a plot.

test_plot_bar_chart_invalid_data: This test evaluates the behavior of the plot_bar_chart function when the required "Nature" column is missing from the input data. A DataFrame is created without the "Nature" column (instead using "Type"). The function is called, and the test asserts that the function should return None when the "Nature" column is absent, indicating that the function is properly handling invalid input.

## Bugs and Assumptions
1) The code assumes that all PDF files follow a consistent format, with certain fields such as "Incident Time", "Incident Number", "Location", "Nature", and "ORI". If the structure of the PDFs changes, the extraction logic in extract_data_from_pdf may break.

2) The code assumes that users will upload PDFs or provide URLs in a correct format, without much input validation. It does not handle cases where users upload files with incorrect extensions or provide malformed URLs.

3) The code assumes that once the data is extracted and processed into a DataFrame, it will be clean enough to generate visualizations. However, any discrepancies in the data (such as missing "Nature" or "Count" fields) could cause issues in subsequent processing steps.

4) The clustering function uses a fixed number of clusters (3) in KMeans. While this is a reasonable default, it assumes that 3 clusters will always be appropriate for the data, which may not be the case in every situation.

5)  No handling of simultaneous requests; this might cause issues when multiple users are uploading or accessing data at the same time.




 


