from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app) # This allows your HTML file to talk to this Python script

@app.route('/api/stats')
def get_stats():
    # Get Real-time Data
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    # Send it as a JSON "Package"
    return jsonify({
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "status": "Healthy" if cpu < 80 else "Overloaded"
    })

if __name__ == '__main__':
    print("🚀 Favour-Watch Server is running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)