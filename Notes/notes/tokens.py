from binascii import hexlify
from os import urandom

def create_api_token():
    return hexlify(urandom(20)).decode()

# if __name__ == '__main__':
#     for i in range(5):
#         print(create_api_token())