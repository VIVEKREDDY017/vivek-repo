from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML templates

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
