import matplotlib
matplotlib.use('Agg')  # Ensure no GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
import io

def cluster_incidents(data, num_clusters=3):
   
    if not isinstance(data, pd.DataFrame):
        print("Error: Expected a pandas DataFrame.")
        return None

    if "Nature" not in data.columns:
        print("Error: 'Nature' column is missing.")
        return None

    nature_counts = data["Nature"].value_counts().reset_index()
    nature_counts.columns = ['Nature', 'Count']

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    nature_counts["Cluster"] = kmeans.fit_predict(nature_counts[['Count']])

    img = io.BytesIO()
    
    plt.figure(figsize=(12, 7))
    
    sns.scatterplot(data=nature_counts, x="Nature", y="Count", hue="Cluster", palette="tab10", s=150, edgecolor="black")
    
    plt.title("Incident Clustering (Based on Nature)", fontsize=16)
    plt.xlabel("Incident Nature", fontsize=14)
    plt.ylabel("Incident Count", fontsize=14)
    
    plt.xticks(rotation=45, ha="right", fontsize=12)
    
    plt.legend(title="Cluster", fontsize=12, title_fontsize=14, loc="upper right")
    
    plt.tight_layout()

    plt.savefig(img, format='png')
    img.seek(0)  
    plt.close()  
    
    return img  
