# amqps://rkwmdwnd:x0_grWOL-Wi1DEfzv7BSGJToQ70IGby4@puffin.rmq2.cloudamqp.com/rkwmdwnd
from logging import exception
import pika, json


params = pika.URLParameters('amqps://rkwmdwnd:x0_grWOL-Wi1DEfzv7BSGJToQ70IGby4@puffin.rmq2.cloudamqp.com/rkwmdwnd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    try:
        channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    except exception as error:
        print(error)
        
