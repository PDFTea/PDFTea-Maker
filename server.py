<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "PDFTea Maker Development Server is Running!"

# Example endpoint for Canva webhook testing
@app.route("/canva-webhook", methods=["POST"])
def canva_webhook():
    data = request.json
    print("Received data from Canva:", data)
    return jsonify({"status": "success"}), 200

# Example endpoint to fetch templates
@app.route("/templates", methods=["GET"])
def get_templates():
    # Example response; replace with actual logic to fetch templates
    templates = [
        {"id": "template_1", "name": "Basic Template"},
        {"id": "template_2", "name": "Advanced Template"}
    ]
    return jsonify({"templates": templates})

# Example endpoint for searching assets
@app.route("/search-assets", methods=["GET"])
def search_assets():
    query = request.args.get("query", "")
    # Example response; replace with logic to search Canva or other integrations
    assets = [
        {"id": "asset_1", "name": f"Asset matching '{query}'"},
        {"id": "asset_2", "name": "Generic Asset"}
    ]
    return jsonify({"assets": assets})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
=======
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "PDFTea Maker Development Server is Running!"

# Example endpoint for Canva webhook testing
@app.route("/canva-webhook", methods=["POST"])
def canva_webhook():
    data = request.json
    print("Received data from Canva:", data)
    return jsonify({"status": "success"}), 200

# Example endpoint to fetch templates
@app.route("/templates", methods=["GET"])
def get_templates():
    # Example response; replace with actual logic to fetch templates
    templates = [
        {"id": "template_1", "name": "Basic Template"},
        {"id": "template_2", "name": "Advanced Template"}
    ]
    return jsonify({"templates": templates})

# Example endpoint for searching assets
@app.route("/search-assets", methods=["GET"])
def search_assets():
    query = request.args.get("query", "")
    # Example response; replace with logic to search Canva or other integrations
    assets = [
        {"id": "asset_1", "name": f"Asset matching '{query}'"},
        {"id": "asset_2", "name": "Generic Asset"}
    ]
    return jsonify({"assets": assets})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
>>>>>>> 9dc5a799b5806699c835ddd26bc650c5b63f2801
=======
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "PDFTea Maker Development Server is Running!"

# Example endpoint for Canva webhook testing
@app.route("/canva-webhook", methods=["POST"])
def canva_webhook():
    data = request.json
    print("Received data from Canva:", data)
    return jsonify({"status": "success"}), 200

# Example endpoint to fetch templates
@app.route("/templates", methods=["GET"])
def get_templates():
    # Example response; replace with actual logic to fetch templates
    templates = [
        {"id": "template_1", "name": "Basic Template"},
        {"id": "template_2", "name": "Advanced Template"}
    ]
    return jsonify({"templates": templates})

# Example endpoint for searching assets
@app.route("/search-assets", methods=["GET"])
def search_assets():
    query = request.args.get("query", "")
    # Example response; replace with logic to search Canva or other integrations
    assets = [
        {"id": "asset_1", "name": f"Asset matching '{query}'"},
        {"id": "asset_2", "name": "Generic Asset"}
    ]
    return jsonify({"assets": assets})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
>>>>>>> 9dc5a799b5806699c835ddd26bc650c5b63f2801
