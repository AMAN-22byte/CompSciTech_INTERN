package com.example.spring_mq_ij.controller;

import com.example.spring_mq_ij.publisher.RabbitMQProducer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class CalculatorController {

    private final RabbitMQProducer rabbitMQProducer;

    @Autowired
    public CalculatorController(RabbitMQProducer rabbitMQProducer) {
        this.rabbitMQProducer = rabbitMQProducer;
    }

    @RequestMapping("/")
    public String index() {
        return "index";
    }

    @PostMapping("/calculate")
    public String calculate(
            @RequestParam int operand1,
            @RequestParam int operand2,
            @RequestParam String operator,
            Model model) {
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
                    result = operand1 / (double) operand2;
                } else {
                    model.addAttribute("error", "Cannot divide by zero");
                    return "index";
                }
                break;
        }
        rabbitMQProducer.sendMessage(operand1 + "," + operand2 + "," + operator);
        model.addAttribute("result", result);
        return "index";
    }
}
