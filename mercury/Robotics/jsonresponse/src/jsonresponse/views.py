from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt


def send_json(request):

    data = {'Failer_Mode': "0", 'arm1': '0',
             'arm2': '1', 'travel': '0', 'steering': '0', 'rotate_hand1': '0', 'rotate_hand2': "0",
            'elbow1': '0', 'elbow2': '0', 'talk': '0', 'hand1_all': '0', 'hand2_all': '0'}

    return JsonResponse(data, safe=False)


# Create your views here.


