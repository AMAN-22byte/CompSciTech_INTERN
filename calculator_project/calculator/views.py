from django.shortcuts import render
from .utils import add, subtract, multiply, divide

def calculator(request):
    result = None
    if request.method == 'POST':
        operand1 = float(request.POST.get('operand1'))
        operand2 = float(request.POST.get('operand2'))
        operator = request.POST.get('operator')
        if operator == 'add':
            result = add(operand1, operand2)
        elif operator == 'subtract':
            result = subtract(operand1, operand2)
        elif operator == 'multiply':
            result = multiply(operand1, operand2)
        elif operator == 'divide':
            result = divide(operand1, operand2)
    return render(request, 'calculator.html', {'result': result})
