# amqps://rkwmdwnd:x0_grWOL-Wi1DEfzv7BSGJToQ70IGby4@puffin.rmq2.cloudamqp.com/rkwmdwnd
import pika

params = pika.URLParameters('amqps://rkwmdwnd:x0_grWOL-Wi1DEfzv7BSGJToQ70IGby4@puffin.rmq2.cloudamqp.com/rkwmdwnd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming...")

channel.start_consuming()


channel.close()