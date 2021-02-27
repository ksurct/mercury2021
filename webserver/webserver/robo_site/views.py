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
    else:
        robot = ret
        return HttpResponse(computer)

def test(request):
    return HttpResponse("This is a test")

def main(request):
    return HttpResponse("This is a test")