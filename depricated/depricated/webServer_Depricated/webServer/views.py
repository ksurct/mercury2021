from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

controllerInfo = models.ControllerInformation()

@csrf_exempt
def c_index(request):
    return HttpResponse("Default index.\n" + str(controllerInfo))

@csrf_exempt
def c_updateController(request):
    if ('updateDict' in request.POST.keys()):
        ret = controllerInfo.updateController(json.loads(request.POST['updateDict']))
        if (ret == ''):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=422, content=ret)

@csrf_exempt
def c_getController(request):
    return HttpResponse(content=json.dumps(controllerInfo.toDict()), status=200)