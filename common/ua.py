from common import ua_list
import random

def get_ua():
    return random.choice(ua_list)

if __name__ == '__main__':
    print(get_ua())