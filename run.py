from app import create_app

# Create an instance of the application using the factory function `create_app`
app = create_app()

if __name__ == '__main__':
    """
    Run the Flask application in debug mode if the script is executed directly.

    When `app.run(debug=True)` is called:
    - The application will start in development mode.
    - Debug mode provides useful error messages and auto-reloads the app when code changes.
    """
    app.run(debug=True)
