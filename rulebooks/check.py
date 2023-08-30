#!/usr/bin/python

import hashlib
from kafka import KafkaProducer

def main():
    file_path = '/opt/test.conf'
    prev_digest = '7db113973333158444af0a91d22be19088eee9830412978815c4f9831ea11227'

    with open(file_path, 'rb') as f:
        binary = f.read()
        digest = hashlib.sha256(binary).hexdigest()

    if prev_digest == digest:
        print("File is not modified")
    else:
        print("File is modified")
        send_message()

def send_message():
    producer = KafkaProducer(bootstrap_servers=['10.9.92.21:9092'])
    future = producer.send('my-topic', key=b'key', value=b'test', partition=0)
    result = future.get(timeout=10)
    print(result)

main()

