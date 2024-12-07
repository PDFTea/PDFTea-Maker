import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Simulated Canva integration
def get_templates():
    return [
        {"id": "template_1", "name": "Modern Presentation"},
        {"id": "template_2", "name": "Business Report"}
    ]

def create_design(template_id):
    return {"design_id": f"design_{template_id}", "status": "success"}

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to PDFTea Maker!"})

@app.route("/canva/templates", methods=["GET"])
def fetch_templates():
    templates = get_templates()
    return jsonify({"templates": templates})

@app.route("/canva/design", methods=["POST"])
def generate_design():
    data = request.json
    if not data or "template_id" not in data:
        return jsonify({"error": "Missing 'template_id'"}), 400
    design = create_design(data["template_id"])
    return jsonify({"message": "Design created successfully", "design": design})

if __name__ == "__main__":
    app.run(debug=True)
