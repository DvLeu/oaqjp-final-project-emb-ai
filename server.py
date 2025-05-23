"""
Here we import all libraries used in this project
"""
from flask import Flask, request, render_template, make_response
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route('/')
def index():
    """
    Default index.html template to execute
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def analyze_emotion():
    """
    This method will get the response based on the user input
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger, disgust, fear, joy, sadness = (
    response['anger'],
    response['disgust'],
    response['fear'],
    response['joy'],
    response['sadness']
)

    dominant_emotion = response['dominant_emotion']
    response = (
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
    f"'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
)


    if dominant_emotion is None:
        return make_response("Invalid text! Please try again!", 400)
    return response



if __name__ == '__main__':
    app.run(debug=True, port=5000)
