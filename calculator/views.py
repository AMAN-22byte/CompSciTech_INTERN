from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def calculate(request):
    
    if request.method == 'POST':
        operand1 = float(request.POST.get('operand1'))
        operand2 = float(request.POST.get('operand2'))
        operator = request.POST.get('operator')

        # Perform calculation based on operator
        if operator == 'add':
            result = operand1 + operand2
        elif operator == 'subtract':
            result = operand1 - operand2
        elif operator == 'multiply':
            result = operand1 * operand2
        elif operator == 'divide':
            result = operand1 / operand2
        else:
            return HttpResponse("Invalid operator")

        return HttpResponse(f"Result: {result}")
    else:
        return HttpResponse("Calculator Form")