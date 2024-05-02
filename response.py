from twilio.twiml.voice_response import VoiceResponse
import os
from flask import Flask
secret_key = str(os.urandom(24))
app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key

@app.route('/voice', methods=["POST"])
def voice():
    resp = VoiceResponse()
    audio = "Hello! This is the Driver"
    resp.say(audio, voice='male')
    resp.hangup()
    return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)