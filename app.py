from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'YOUR_YOUTUBE_API_KEY'
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    if request.method == 'POST':
        query = request.form.get('query')
        params = {
            'part': 'snippet',
            'q': query,
            'key': API_KEY,
            'type': 'video',
            'maxResults': 5
        }
        response = requests.get(SEARCH_URL, params=params)
        results = response.json().get('items', [])
        for result in results:
            video_data = {
                'title': result['snippet']['title'],
                'description': result['snippet']['description'],
                'thumbnail': result['snippet']['thumbnails']['high']['url'],
                'url': f"https://www.youtube.com/embed/{result['id']['videoId']}"
            }
            videos.append(video_data)
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
