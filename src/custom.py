import matplotlib.pyplot as plt
import seaborn as sns
import io

def plot_custom_pie_chart(data):
    """
    Custom visualization: Pie chart of incidents by type (Nature).
    """
    if "Nature" not in data.columns:
        print("Error: The dataset must contain a 'Nature' column for pie chart visualization.")
        return None  # Return None if data is invalid

    # Calculate incident type counts
    incident_counts = data["Nature"].value_counts()

    # Generate a color palette using seaborn
    try:
        colors = sns.color_palette("Set3", n_colors=len(incident_counts))
    except Exception as e:
        print(f"Error generating color palette: {e}")
        colors = plt.cm.Paired.colors  # Fallback to default colors if necessary

    # Plot pie chart
    plt.figure(figsize=(10, 10))  # Increase figure size
    incident_counts.plot(kind="pie", autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})

    # Make sure the chart is tight and doesn't overlap
    plt.title("Incident Type Distribution (Nature)", fontsize=16)
    plt.ylabel("")  # Hide the y-label
    plt.gca().set_aspect('equal')  # Ensure the pie chart is circular

    # Use tight_layout to avoid overlaps
    plt.tight_layout()

    # Save the plot to a BytesIO object to avoid calling plt.show()
    img = io.BytesIO()
    plt.savefig(img, format='png')  # Save the plot to the buffer
    img.seek(0)  # Reset the pointer to the beginning of the image buffer
    plt.close()  # Close the plot to free memory

    return img  # Return the image buffer
