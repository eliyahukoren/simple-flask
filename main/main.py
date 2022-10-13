from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Simple Flask app'


if __name__ == '__main__':
    port = os.environ.get("PORT", 5001)
    app.run(debug=True, host='0.0.0.0', port=port)