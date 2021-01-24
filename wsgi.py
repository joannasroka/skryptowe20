import os

from lab5_solutions.api import app
from flask_cors import CORS

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    CORS(app)
    app.run(debug=True, port=port)
