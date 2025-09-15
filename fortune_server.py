from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os
import random
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from fortune_list import FORTUNES_LIST

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # allow frontend and backend to talk across domains

@app.route("/")
def index():
    # Serve the main HTML file (make sure it’s in a /templates folder)
    return render_template("magic_mike.html")

@app.route("/fortune")
def get_fortune():
    # Return a random fortune as JSON
    fortune = random.choice(FORTUNES_LIST)
    return jsonify({"fortune": fortune})

if __name__ == "__main__":
    # Render provides the port in an environment variable
    port = int(os.environ.get("PORT", 5001))  # 5001 is fallback for local dev
    app.run(host="0.0.0.0", port=port)
