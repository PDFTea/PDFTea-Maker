from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Example route
@app.route("/")
def home():
    return jsonify(message="Welcome to PDFTea Maker!")

@app.route("/api/example", methods=["POST"])
def example():
    data = request.json
    return jsonify(received_data=data)

# Main entry point for the application
if __name__ == "__main__":
    import os
    # Dynamically assign the port from environment variables (default to 8000)
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
