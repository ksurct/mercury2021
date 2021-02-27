from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

computer = "you are the robot"
robot = "you are the computer"

def robo_site(request, blob):
    global computer, robot
    print(blob)
    ret = blob.split(',')
    ret.pop(0)
    ret = ",".join(ret)
    if (blob.split(',')[0] == 'computer'):
        computer = ret
        return HttpResponse(robot)
    elif (blob.split(',')[0] == 'robot'):
        robot = ret
        return HttpResponse(computer)
    else:
        return HttpResponse("Unknown entity")

def test(request):
    return HttpResponse("This is a test")

def main(request):
    return HttpResponse("This is a test")