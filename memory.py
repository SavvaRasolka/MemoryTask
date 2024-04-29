import psutil
import argparse
import urllib.request
import json
import time


def alarm(url, level):
    try:
        alarm_data = json.dumps({'alarm': f'Memory level more than {str(level)}'}).encode('utf-8')
        request = urllib.request.Request(url, data=alarm_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(request) as response:
            if response.getcode() == 200:
                print('Alarm sent')
                return True
            else:
                print(f'Failed to send alarm. Status code: {response.getcode()}')
                return False
    except Exception as e:
        print(f'An error occurred while sending alarm: {e}')
        return False


def main(memory_limit, address, time_delay):
    while True:
        if psutil.virtual_memory().percent > memory_limit:
            alarm(address, memory_limit)
        time.sleep(time_delay)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alert memory level')
    parser.add_argument('limit', type=str, help='Input memory limit in percent')
    parser.add_argument('address', type=str, help='API address to send alarm')
    parser.add_argument('time', type=str, help='Period of scan in second')
    args = parser.parse_args()
    print(f'Start monitoring memory with limit {str(args.limit)} percent')
    main(int(args.limit), args.address, int(args.time))
