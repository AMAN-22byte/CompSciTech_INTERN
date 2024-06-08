package com.example.spring_mq_ij.config;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.TopicExchange;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    @Value("${rabbitmq.queue.name}")
    private String queue;
    @Value("${rabbitmq.exchange.name}")
    private String exchange;
    @Value("${rabbitmq.routingKey.name}")
    private String routingKey;
    //spring bean for mq queue
    @Bean
    public Queue queue(){
        return new Queue(queue);
    }
    @Bean
    //spring bean for mq exchange
    public TopicExchange exchange(){
        return new TopicExchange(exchange);
    }

    //bind queue with exchange
    @Bean
    public Binding binding(){
        return BindingBuilder.bind(queue())
                .to(exchange())
                .with(routingKey);
    }
    //ALL THESE ARE AUTO CONFIGURED....
    //connection factory
    //rabbit template
    //rabbit admin
}
