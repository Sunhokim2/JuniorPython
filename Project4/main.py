from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("in2.html")

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_data = requests.get(age_url).json()
    age = age_data['age']
    return render_template('guess.html', person_name=name,gender=gender,age=age)

if __name__=="__main__":
    app.run(debug=True)