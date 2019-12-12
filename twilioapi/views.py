from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient, Client
from twilio.twiml.voice_response import VoiceResponse
import os
from django.conf import settings




@twilio_view
def user_call(request):
    account_sid=os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token=os.environ.get("TWILIO_AUTH_TOKEN")
    client=Client(account_sid,auth_token)
    call=client.calls.create(
        to="+919354531933",
        from_="+12512441313",
        url="http://demo.twilio.com/docs/voice.xml",
        method='GET'
    )
    return redirect(gather_digits)

@twilio_view
def gather_digits(request):
    msg = 'Press 1 for text and 2 for voice'
    twilio_response=VoiceResponse ()

    with twilio_response.gather(Action='/respond', numDigits=1) as g:
        g.say(msg)
        g.pause(length=1)
        g.say(msg)

    return redirect(handle_response,twilio_response)


@twilio_view
def handle_response(request):

    digits=request.POST.get('Digits', '')

    twilio_response=VoiceResponse()

    if digits=='1':
        twilio_response.play('http://bit.ly/phaltsw')

    if digits == '2':
        number.request.POST.get('From','')
        twilio_response.say('Text Message')
        twilio_response.sms('Issue',to=number)

    return twilio_response
