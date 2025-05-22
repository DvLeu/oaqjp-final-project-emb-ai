from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def analyze_emotion():
    if request.method == 'POST' : 
        text_to_analyze = request.form.get('textToAnalyze')
    else :
        text_to_analyze = request.args.get('textToAnalize')
    result = emotion_detector(text_to_analyze)
    if "error" in result :
        return "Error" + result["error"]  
    
    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return formatted

if __name__ == '__main__':
    app.run(debug=True, port=5000)