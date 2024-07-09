package com.example.spring_mq_ij.consumer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class RabbitMQConsumer {

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQConsumer.class);

    @Value("${rabbitmq.queue.name}")
    private String queueName;

    @RabbitListener(queues = "${rabbitmq.queue.name}")
    public void consumeMessage(String message) {
        LOGGER.info(String.format("Message received from RabbitMQ queue '%s': %s", queueName, message));
        // Here you can perform the calculation and print the output
        // For simplicity, let's assume the message contains operands and operator separated by comma
        String[] parts = message.split(",");
        if (parts.length == 3) {
            int operand1 = Integer.parseInt(parts[0]);
            int operand2 = Integer.parseInt(parts[1]);
            String operator = parts[2];
            double result = 0;
            switch (operator) {
                case "+":
                    result = operand1 + operand2;
                    break;
                case "-":
                    result = operand1 - operand2;
                    break;
                case "*":
                    result = operand1 * operand2;
                    break;
                case "/":
                    if (operand2 != 0) {
                        result = (double) operand1 / operand2;
                    } else {
                        LOGGER.error("Cannot divide by zero");
                    }
                    break;
                default:
                    LOGGER.error("Invalid operator");
            }
            LOGGER.info(String.format("Calculation result: %d %s %d = %.2f", operand1, operator, operand2, result));
        } else {
            LOGGER.error("Invalid message format");
        }
    }
}
