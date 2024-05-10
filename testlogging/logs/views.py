from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def add_numbers(request):
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            result = num1 + num2
            logger.info(f"Addition performed: {num1} + {num2} = {result}")
            return HttpResponse(f'The result of {num1} + {num2} is {result}')
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            return HttpResponse("Error occurred while adding the numbers.")
    else:
        return render(request, 'index.html')
def index(request):
    if request.method == 'POST':
        # Handle POST request
        return HttpResponse("Received a POST request")
    else:
        # Handle GET request (rendering the template)
        return render(request, 'index.html')