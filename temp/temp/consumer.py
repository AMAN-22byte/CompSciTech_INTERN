# consumer/consumer.py

import json
from channels.generic.websocket import WebsocketConsumer
from .models import CalculationRequest
from .calculator import calculate

class CalculationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        num1 = data['num1']
        num2 = data['num2']
        opr = data['opr']

        # Perform the calculation
        result = calculate(num1, num2, opr)

        # Send the result back to the client
        self.send(text_data=json.dumps({'result': result}))
