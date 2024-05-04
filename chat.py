from flask import Flask, request, render_template, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import bot

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
    session['state'] = 'start'
    return render_template('index.html')

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    resp.message().body(bot.generate_response(incoming_msg))
    
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
