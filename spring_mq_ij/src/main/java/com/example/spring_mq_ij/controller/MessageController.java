package com.example.spring_mq_ij.controller;

import com.example.spring_mq_ij.publisher.RabbitMQProducer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.util.UriUtils;

@RestController
public class MessageController {

    private final RabbitMQProducer producer;

    @Autowired
    public MessageController(RabbitMQProducer producer) {
        this.producer = producer;
    }

    @GetMapping("/api/v1/publish")
    public ResponseEntity<String> sendMessage(@RequestParam("message") String message) {
        try {
            producer.sendMessage(message);
            return ResponseEntity.ok("Message sent to RabbitMQ: " + message);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Failed to send message to RabbitMQ: " + message);
        }
    }
}
