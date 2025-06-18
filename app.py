from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ YouTube Transcript API is live!"

@app.route('/transcript')
def transcript():
    url = request.args.get("video", "")
    video_id = ""

    # Handle different YouTube URL formats
    if "youtube.com/watch?v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com/live/" in url:
        video_id = url.split("youtube.com/live/")[1].split("?")[0]
    else:
        return jsonify({"error": f"Could not extract video ID from URL: {url}"}), 400

    try:
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
