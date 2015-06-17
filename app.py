from flask import Flask, make_response
from bs4 import BeautifulSoup
from zipfile import ZipFile

html_doc = 'http://10.5.5.9:80'  # This is where the GoPro server hosts files
soup = BeautifulSoup(html_doc)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# From: http://code.runnable.com/UiIdhKohv5JQAAB6/
# how-to-download-a-file-generated-on-the-fly-in-flask-for-python
# This route will prompt a file download with the csv lines
@app.route('/download')
def download():

    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
    "1985/01/21","Douglas Adams",0345391802,5.95
    "1990/01/12","Douglas Hofstadter",0465026567,9.95
    "1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
    "1999/12/03","Richard Friedman",0060630353,5.95
    "2004/10/04","Randel Helms",0879755725,4.50"""

    directory = 'directory'
    filename = 'GoPro_' + directory + '.zip'

    with ZipFile(filename, 'w') as myzip:
        myzip.write(csv)

    # We need to modify the response, so the first thing we
    # need to do is create a response out of the CSV string
    response = make_response(myzip)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = \
        "attachment; filename=" + filename
    return response


if __name__ == "__main__":
    app.run()
