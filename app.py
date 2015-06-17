from flask import Flask
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
