import pika
import time

RABBITMQ_HOST = 'rabbitmq'
ALERT_QUEUE = 'lightAlertQueue'

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=ALERT_QUEUE)

        def callback(ch, method, properties, body):
            alert_message = body.decode()
            print(f"Alert received: {alert_message}")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=ALERT_QUEUE, on_message_callback=callback)
        print("Alert Client started. Waiting for alerts...")
        channel.start_consuming()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == '__main__':
    main()