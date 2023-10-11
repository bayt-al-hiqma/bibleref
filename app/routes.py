from app import app
import requests
import json
from flask import render_template, request, redirect, url_for

BIBLE_IDS = ["9879dbb7cfe39e4d-02", "65eec8e0b60e656b-01", "7142879509583d59-01"]

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = "ba85c47cb54b17cf4016e5c62ef0bb4c"
    headers = {'api-key': api_key}

    # Fetch the list of available books for the first Bible ID as a sample
    books_url = f"https://api.scripture.api.bible/v1/bibles/{BIBLE_IDS[0]}/books"
    books_response = requests.get(books_url, headers=headers)
    books_data = json.loads(books_response.text)
    available_books = [book['name'] for book in books_data['data']]

    if request.method == 'POST':
        selected_bible_id = request.form['bible_id']
        book = request.form['book']
        chapter = request.form['chapter']
        verse = request.form['verse']

        # Fetch the verse for each Bible ID
        verse_data = {}
        for bible_id in BIBLE_IDS:
            verse_url = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/verses/{book}.{chapter}.{verse}"
            verse_response = requests.get(verse_url, headers=headers)
            if verse_response.status_code == 200:
                verse_json = json.loads(verse_response.text)
                verse_data[bible_id] = verse_json['data']['content']
            else:
                verse_data[bible_id] = "Verse not found"

        return render_template('result.html', verse_data=verse_data)

    return render_template('index.html', available_books=available_books)
