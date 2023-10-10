from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        chapter = request.form['chapter']
        verse = request.form['verse']
        bible_verse = fetch_bible_verse(chapter, verse)
        return render_template('result.html', bible_verse=bible_verse)
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

def fetch_bible_verse(chapter, verse):
    api_key = "ba85c47cb54b17cf4016e5c62ef0bb4c"
    headers = {'api-key': api_key}
    # Replace BIBLE_ID with the specific Bible version ID you want to use
    # de4e12af7f28f599-02 is the ID for King James Version
    api_url = f"https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-02/passages/{chapter}.{verse}"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']['content']
    else:
        return "Verse not found"

if __name__ == '__main__':
    app.run(debug=True)
