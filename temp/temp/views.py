# producer/views.py

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CalculationRequest
from .producer import publish_message

@csrf_exempt
def generate_calculation_request(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = float(data['num1'])
            num2 = float(data['num2'])
            opr = data['opr']

            # Save the calculation request to the database (optional)
            calculation_request = CalculationRequest.objects.create(num1=num1, num2=num2, opr=opr)
            calculation_request.save()

            # Publish the calculation request to the message broker
            publish_message({'num1': num1, 'num2': num2, 'opr': opr})

            return JsonResponse({'message': 'Calculation request sent successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)
