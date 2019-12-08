from django_twilio.decorators import twilio_view

from twilio.twiml.voice_response import VoiceResponse

@twilio_view
def gather_digits(request):
    msg = 'Press 1 for text and 2 for voice'
    twilio_response=VoiceResponse()

    with twilio_response.gather(Action='/respond', numDigits=1) as g:
        g.say(msg)
        g.pause(length=1)
        g.say(msg)

    return twilio_response


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