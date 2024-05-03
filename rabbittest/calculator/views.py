from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def add(request):
    operand1 = float(request.GET.get('operand1'))
    operand2 = float(request.GET.get('operand2'))
    result = operand1 + operand2
    return HttpResponse(f"The result of addition is: {result}")

def subtract(request):
    operand1 = float(request.GET.get('operand1'))
    operand2 = float(request.GET.get('operand2'))
    result = operand1 - operand2
    return HttpResponse(f"The result of subtraction is: {result}")

def multiply(request):
    operand1 = float(request.GET.get('operand1'))
    operand2 = float(request.GET.get('operand2'))
    result = operand1 * operand2
    return HttpResponse(f"The result of multiplication is: {result}")

def divide(request):
    operand1 = float(request.GET.get('operand1'))
    operand2 = float(request.GET.get('operand2'))
    result = operand1 / operand2
    return HttpResponse(f"The result of division is: {result}")