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

    if "watch?v=" in url:
        video_id = url.split("watch?v=")[-1]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1]
    else:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    try:
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
