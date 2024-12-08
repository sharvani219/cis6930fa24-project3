import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import io

def plot_bar_graph(data):
    if "Nature" not in data.columns:
        print("Error: The dataset must contain a 'Nature' column for bar chart visualization.")
        return None  

    img = io.BytesIO()
    
    plt.figure(figsize=(12, 7))  
    data["Nature"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    
    plt.title("Frequency of Incident Types (Nature)", fontsize=16)
    plt.xlabel("Incident Type (Nature)", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    
    plt.xticks(rotation=45, ha="right", fontsize=12)
    
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)  
    plt.close()  

    return img  
