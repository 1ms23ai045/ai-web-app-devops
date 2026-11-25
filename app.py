
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home page - Course Registration System
@app.route("/")
def home():
    return render_template("index.html")

# Health check - used by Docker and deployment monitoring
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Course Registration System"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
