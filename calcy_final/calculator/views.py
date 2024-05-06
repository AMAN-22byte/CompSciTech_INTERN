from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from .producer import send_message
from .producer import send_message
from .consumer import calculation_result 

def calculate(request):
    if request.method == 'POST':
        operator = request.POST.get('operator')
        operand1 = request.POST.get('operand1')
        operand2 = request.POST.get('operand2')

        message = f"{operator},{operand1},{operand2}"
        send_message(message)
        return HttpResponse("Calculation request sent to RabbitMQ.")

    else:
        return render(request, 'index.html')


def get_result(request):
    global calculation_result

    if calculation_result is not None:
        result = calculation_result
        calculation_result = None  
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'result': None})