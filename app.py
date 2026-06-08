from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is the message that will display on your screen when you visit the website
    return "<h1>🚀 Jenkins to Docker Hub CI/CD Pipeline Working Successfully!</h1>"

if __name__ == '__main__':
    # Runs the application on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)

