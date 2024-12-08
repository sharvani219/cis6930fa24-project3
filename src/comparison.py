import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import io

def plot_bar_graph(data):
    """
    Plots a bar chart comparing the frequency of incident types (Nature) and returns the plot image.
    """
    if "Nature" not in data.columns:
        print("Error: The dataset must contain a 'Nature' column for bar chart visualization.")
        return None  # Return None if the data is invalid

    # Create the plot in memory
    img = io.BytesIO()
    
    # Set figure size for better readability
    plt.figure(figsize=(12, 7))  # Increase figure size for clarity
    
    # Plot the bar chart with the desired style
    data["Nature"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    
    # Title and labels with increased font size
    plt.title("Frequency of Incident Types (Nature)", fontsize=16)
    plt.xlabel("Incident Type (Nature)", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    
    # Rotate the x-axis labels for better readability and prevent overlap
    plt.xticks(rotation=45, ha="right", fontsize=12)
    
    # Ensure that the layout doesn't overlap or get cut off
    plt.tight_layout()
    
    # Save the plot to the in-memory buffer
    plt.savefig(img, format='png')
    img.seek(0)  # Reset the pointer to the beginning of the image buffer
    plt.close()  # Close the plot to free memory

    return img  # Return the image buffer
