# app.py
from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import scipy.signal as signal
import numpy as np

app = Flask(__name__)

# Route for serving the HTML file
@app.route('/')
def home():
    return render_template('voice_search.html')

# Route for processing the voice query
@app.route('/search', methods=['POST'])
def process_query():
    data = request.get_json()
    query = data.get('query')

    # Example of processing (mock DSP or text processing)
    processed_query = query.lower()
    
    # Simulated search result
    results = {
        "query": processed_query,
        "results": [
            {"title": "Result 1", "url": "/result1"},
            {"title": "Result 2", "url": "/result2"}
        ]
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
