import requests
import json

from flask import Flask, render_template, request
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        
        inputted_course = request.form["course"]
        url = "https://utsc.calendar.utoronto.ca/course/" + inputted_course + "H3"

        try:
            if (requests.get(url).request.url == "https://utsc.calendar.utoronto.ca/sorry-course-has-been-retired-and-no-longer-offered"):
                message = json.dumps({"message": "We could not find the inputted course. Please try again.", "status":404})
                return render_template('index.html', message=message)
            course = {}
            text = requests.get(url).text
            soup = BeautifulSoup(text, "html5lib")
            course["Course"] = soup.find_all("h1", {"class": "title"})[0].text.strip()
            course["Description"] = soup.find_all("div", {"class": "field-item even"})[0].text.strip()
            course["Prerequiste"] = soup.find_all("div", {"class": "field-item even"})[1].text.strip()
            course["Exclusion"] = soup.find_all("div", {"class": "field-item even"})[2].text.strip()
            course["Breadth"] = soup.find_all("div", {"class": "field-item even"})[3].text.strip()
            course["status"] = 200
            message = json.dumps(course)
            return render_template('index.html', message=message)
        except Exception as e:
            print(e)
            message = json.dumps({"message": "There was an error. The error is " + e, "status":400})
            return render_template('index.html', message=message)

    return render_template('index.html')
    

if (__name__ == "__main__"):
	# Creates a secret key.
	app.secret_key = b"secretkey"
	app.run(debug = True)