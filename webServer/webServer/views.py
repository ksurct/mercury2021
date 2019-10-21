from django.http import HttpResponse
from . import models

controllerInfo = models.ControllerInformation()

def index(request):
    return HttpResponse("Default index.\n" + str(controllerInfo))