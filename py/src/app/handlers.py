import os

__VALID_REQUESTS__ = [
    'lowercase',
    'uppercase',
    'reverse',
    'randomcase'
]

def __entry__(req, payload):
    if req not in __VALID_REQUESTS__:
        return f'Error 500: unknown request: {req}'
    if not payload:
        return f'Error 500: empty payload: {payload}'
    func = globals()[req]
    return func(payload.decode('UTF-8'))


def lowercase(s):
    return s.lower()


def uppercase(s):
    return s.upper()


def reverse(s):
    return s[::-1]


def randomcase(s):
    randomized = []
    for i in s:
        is_upper = int.from_bytes(os.urandom(1), byteorder='big') % 2
        if is_upper:
            randomized.append(i.upper())
        else:
            randomized.append(i.lower())
    return ''.join(randomized)
