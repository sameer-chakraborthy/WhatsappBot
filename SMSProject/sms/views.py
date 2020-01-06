from django.shortcuts import render
from sms.models import Table

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    # msg = request.form.get('Body')
    msg = request.POST.get('Body')
    resp = MessagingResponse()
    # Add a text message
    resp.message("Thank you, lead created.")
    

    for x in msg.splitlines():
    	field = x.split(':')[0].strip().lower()
    	value = x.split(':')[1].rstrip().lstrip()
        
    	if field == "name":
                name_=value
    	if field == "location":
                location_=value
    	if field == "product":
                product_=value
    	if field == "mobile":
                mobile_=value
    	if field == "amount":
                amount_=value
    b = Table(name=name_,location=location_,product=product_,mobile=mobile_,amount=amount_)
    b.save()	
    return HttpResponse(resp)

# def sms_response1(request):
# 	resp = MessagingResponse()
# 	resp.message("Thank you, lead created")
# 	return HttpResponse(resp)
