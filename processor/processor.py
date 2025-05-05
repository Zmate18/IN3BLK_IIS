import pika
import time

RABBITMQ_HOST = 'rabbitmq'
SOURCE_QUEUE = 'lightIntensityQueue'
ALERT_QUEUE = 'lightAlertQueue'

def main():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=SOURCE_QUEUE)
        channel.queue_declare(queue=ALERT_QUEUE)

        low_light_count = [0]

        def callback(ch, method, properties, body):
            try:
                lux = int(body.decode())
                print(f"Received lux value: {lux}")

                if lux < 100:
                    low_light_count[0] += 1
                else:
                    low_light_count[0] = 0

                if low_light_count[0] >= 3:
                    alert_message = "Low light alert: 3 consecutive readings below 100 lux."
                    channel.basic_publish(exchange='', routing_key=ALERT_QUEUE, body=alert_message)
                    print(f"Sent alert: {alert_message}")
                    low_light_count[0] = 0

            except ValueError:
                print("Invalid data received.")

        channel.basic_consume(queue=SOURCE_QUEUE, on_message_callback=callback, auto_ack=True)
        print("Light Intensity Processor started. Waiting for messages...")
        channel.start_consuming()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()

if __name__ == '__main__':
    main()