from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'appoint.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='',
            recipient_list=['ivangrigorev2817@gmail.com']
        )

        return redirect('appointment:appoint')

