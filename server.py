# Import Flask, render_template, request for the flask framework package
from flask import Flask, render_template, request

#import the EmotionDetection function
from EmotionDetection.emotion_detection import emotion_detector

#inititate the flask app
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''This function initiates rendering of the main app using Flask
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    '''This function receives the text to detect from the HTML interface.
        It then runs the emotion_detector function on it. The ouput shows the 
        scores of the various emotions and the dominate one
    '''
    analysis_text = request.args.get("textToAnalyze")
    result = emotion_detector(analysis_text)
    
    return (f"For the given statement, the system response is 'anger': {result['anger']},"
        f" 'disgust':{result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}"
        f" and 'sadness':{result['sadness']}. The dominant emotion is " 
        f"{result['dominant_emotion']}.")

if __name__ == "__main__":
    '''This function executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port="5000", debug=True)