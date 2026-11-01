from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AI Web Application</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to AI Web Application!</h1>
            <h2>End-to-End DevOps Deployment Project</h2>
            <p>Application Status: Running Successfully</p>
            <p>Powered by Python Flask and Docker</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "AI Web Application",
        "timestamp": datetime.now().isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
