import requests
import string
import random
import os
import time


url = 'http://127.0.0.1'
methods = ('lowercase', 'uppercase', 'randomcase', 'reverse')


while True:
    randlength = int.from_bytes(os.urandom(1), byteorder='big') + 1
    randstring = ''.join(random.choices(string.ascii_lowercase, k = randlength))
    method = random.choice(methods)

    response = requests.post(f'{url}/{method}', randstring.encode('UTF-8'))

    if method == 'lowercase':
        assert response.text == randstring.lower(), f'/lowercase failed: {response.text} != {randstring.lower()}'
    elif method == 'uppercase':
        assert response.text == randstring.upper(), f'/uppercase failed: {response.text} != {randstring.lower()}'
    elif method == 'reverse':
        assert response.text == randstring[::-1], f'/reverse failed: {response.text} != {randstring.lower()}'
    elif method == 'randomcase':
        assert response.text.lower() == randstring.lower(), f'/randomcase failed: {response.text.lower()} != {randstring.lower()}'
    else:
        raise Exception(f'{method} method is unknown')

    print(f'{method}: {randstring}')
    print(f'response: {response.text}')
    print('*' * 50)
    time.sleep(0.5)

