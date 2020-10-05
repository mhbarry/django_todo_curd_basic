from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        msg = request.POST.get('message', '')
        to_email = request.POST.get('to_email', '')
        if msg and to_email:
            send_mail(subject, msg, 'shahriar350@gmail.com', [to_email],    fail_silently=False,)
            messages.success(request,f'Successfully sent message to {to_email}')
        return redirect('mail:index')
    else:
        return render(request, 'mail_index.html')
