import lab5_solutions
from lab5_solutions.api import app
import os
from lab5_solutions.database_repository import *

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)