import json
import re


def func1():
    with open('../JSON.txt', 'r')as fp:
        data = fp.read().strip()
        data = re.findall(r'{"H":.*}', data)
        datalist = [json.loads(i) for i in data]
        print(datalist)


if __name__ == '__main__':
    func1()
