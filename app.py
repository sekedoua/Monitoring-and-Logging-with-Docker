from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Monitoring Docker App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)