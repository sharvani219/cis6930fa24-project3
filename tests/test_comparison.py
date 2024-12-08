import pandas as pd
from io import BytesIO
from src.comparison import plot_bar_graph  

def test_plot_bar_chart_valid_data():
    data = pd.DataFrame({
        'Nature': ['Theft', 'Assault', 'Theft', 'Robbery', 'Theft', 'Assault', 'Assault']
    })
    
    img = plot_bar_graph(data)
    assert isinstance(img, BytesIO), "The function should return a BytesIO object."
    img.seek(0)  
    img_data = img.read()
    assert len(img_data) > 0, "The image data should not be empty."

def test_plot_bar_chart_invalid_data():
    data = pd.DataFrame({
        'Type': ['Theft', 'Assault', 'Robbery', 'Theft']
    })
    
    img = plot_bar_graph(data)
    assert img is None, "The function should return None if 'Nature' column is missing."
    

