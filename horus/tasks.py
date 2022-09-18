from celery import shared_task
from .models import sendEmail
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import sendEmail
from django.conf import settings

@shared_task(blind=True)
def delete_register():
    registers = sendEmail.objects.filter(completo=True)
    for register in registers:
        if register:
            send_mail('Horus econtro estos datos ;)',
            'Ahora estos datos son de su propiedad \n{} \nlo que haga con esta informacion es su responsabilidad.'.format(register.datos),
            settings.EMAIL_HOST_USER,
            ['{}'.format(register.email)],)
            register.delete()
        return "registro eliminado"
    return "no hay ningun registro completado"

@shared_task(blind=True)
def delete_register_expired():
    limite = datetime.now() - timedelta(seconds=3000)
    files = sendEmail.objects.filter(fecha_espera__lte=limite)
    if files:
        files.delete()
        return "archivos eliminados"
    return "no hay archivos expirados"



