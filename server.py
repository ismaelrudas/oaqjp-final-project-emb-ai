"""Servidor Flask para aplication web de emotion detection"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_emotion():
    '''Función que dice que emoción es dominante de acuerdo a la entrada del cliente
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (
    "For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
)
@app.route("/")
def render_index_page():
    ''' Función que renderiza o despliega la página web para que el cliente digite la oración
    a evaluar
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
