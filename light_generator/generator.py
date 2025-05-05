import pika
import random
import time

RABBITMQ_HOST = 'rabbitmq'
QUEUE_NAME = 'lightIntensityQueue'

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)

        print("Light Generator started.")
        while True:
            lux_value = random.randint(0, 2000)
            message = str(lux_value)
            channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=message)
            print(f"Sent: {lux_value} lux")
            time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == '__main__':
    main()