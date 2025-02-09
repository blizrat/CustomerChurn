from flask import Flask
from src.CustomerChurn.logger import logging
from CustomerChurn.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception('Something went wrong')
    except Exception as e:
        obj = CustomException(e, sys)
        logging.info(obj.error_message)
        logging.info("test done")
        return "done"

if __name__ == '__main__':
    app.run(debug = True, port=5002) #port = 5000
