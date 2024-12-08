from src.app import create_app

if __name__ == "__main__":
    # Create the Flask app instance
    app = create_app()
    
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)
