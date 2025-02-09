from flask import Flask
from src.CustomerChurn.logger import logging
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("testing logging file")

    return "done"

if __name__ == '__main__':
    app.run(debug = True, port=5002) #port = 5000
