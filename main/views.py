from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# To send Email ==========>

from django.template.loader import get_template
from django.core.mail import EmailMessage
from portfoliosavej.settings import *

# Create your views here.
def index(request):
    try:
        if request.POST.get('name') != None:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                msg = request.POST.get('message')
                user = Quiry(name = name, email = email , subject = subject, msg = msg)
                user.save()
                messages.info(request,'Request Registered Successfully')
            else:
                return redirect('/')
    except:
        print("except in index page")
        return redirect('/error')
    service = Service.objects.all()
    work = Work.objects.all()
    about = AboutMe.objects.all()

    return render(request,'index.html', {'service':service, 'work':work, 'about': about})
def error_page(request):
    return render(request,'404_not_found.html')

def download(request):
    try:
        about = AboutMe.objects.all()
        for _ in about:
            path = _.cv.name
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
    except:
        return redirect('/error')
