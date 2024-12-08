import matplotlib.pyplot as plt
import seaborn as sns
import io

def plot_custom_pie_chart(data):
    if "Nature" not in data.columns:
        print("Error: The dataset must contain a 'Nature' column for pie chart visualization.")
        return None  

    incident_counts = data["Nature"].value_counts()

    try:
        colors = sns.color_palette("Set3", n_colors=len(incident_counts))
    except Exception as e:
        print(f"Error generating color palette: {e}")
        colors = plt.cm.Paired.colors  

    plt.figure(figsize=(10, 10))  
    incident_counts.plot(kind="pie", autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})
    plt.title("Incident Type Distribution (Nature)", fontsize=16)
    plt.ylabel("")  
    plt.gca().set_aspect('equal')  
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')  
    img.seek(0)  
    plt.close()  

    return img  
