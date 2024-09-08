from django.shortcuts import render
import json
from chaukass.models import Sat
from .form import InputForm
from django.shortcuts import render , redirect
from datetime import datetime
import binascii
# Create your views here.
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "form.html", context)

def submitdata(request):
    if request.method == "POST":
        MyLoginForm = Sat()
        """MyLoginForm.imei=request.POST['imei']
        MyLoginForm.msg=(request.POST['msg'])
        MyLoginForm.lat=request.POST['lat']
        MyLoginForm.long=request.POST['long']
        MyLoginForm.samay=datetime.now()"""
	print(request.POST['iridium_longitude']+binascii.unhexlify(request.POST['data'])
	MyLoginForm.imei=request.POST['imei']
        MyLoginForm.msg=binascii.unhexlify(request.POST['data'])
        MyLoginForm.lat=request.POST['iridium_longitude']
        MyLoginForm.long=request.POST['iridium_latitude']
        MyLoginForm.samay=request.POST['transmit_time']
        MyLoginForm.save()
    else:
        MyLoginForm = Sat()
    return render(request, 'home.html', {'MyLoginForm': MyLoginForm})
def all(request):
    post = Sat.objects.all()
    data = Sat.objects.values('imei', 'msg', 'lat','long','samay')
    date_time=datetime.now()
    json_data = json.dumps(list(data))
    return render(request,"home.html",{'API_KEY':"AIzaSyAChYf5Rs1iR0PpCFkj9i4UazBzAFWhCMs",'jdata':json_data,'post':post,'date_time':date_time})
