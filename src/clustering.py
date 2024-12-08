import matplotlib
matplotlib.use('Agg')  # Ensure no GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
import io

def cluster_incidents(data, num_clusters=3):
    """
    Clusters incident types ('Nature') based on their frequency and returns the plot image.
    """
    if not isinstance(data, pd.DataFrame):
        print("Error: Expected a pandas DataFrame.")
        return None

    if "Nature" not in data.columns:
        print("Error: 'Nature' column is missing.")
        return None

    # Count the occurrences of each nature (incident types)
    nature_counts = data["Nature"].value_counts().reset_index()
    nature_counts.columns = ['Nature', 'Count']

    # Perform clustering using KMeans on the 'Count' column
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    nature_counts["Cluster"] = kmeans.fit_predict(nature_counts[['Count']])

    # Create the plot in memory
    img = io.BytesIO()
    
    # Set figure size for better readability
    plt.figure(figsize=(12, 7))
    
    # Plot the scatter plot using seaborn
    sns.scatterplot(data=nature_counts, x="Nature", y="Count", hue="Cluster", palette="tab10", s=150, edgecolor="black")
    
    # Title and labels with increased font size
    plt.title("Incident Clustering (Based on Nature)", fontsize=16)
    plt.xlabel("Incident Nature", fontsize=14)
    plt.ylabel("Incident Count", fontsize=14)
    
    # Rotate x-axis labels for better readability and prevent overlap
    plt.xticks(rotation=45, ha="right", fontsize=12)
    
    # Increase the size of the legend for clarity
    plt.legend(title="Cluster", fontsize=12, title_fontsize=14, loc="upper right")
    
    # Adjust layout to avoid clipping of labels
    plt.tight_layout()

    # Save the plot to the in-memory buffer
    plt.savefig(img, format='png')
    img.seek(0)  # Reset the pointer to the beginning of the image buffer
    plt.close()  # Close the plot to free memory
    
    return img  # Return the image buffer
