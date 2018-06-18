#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import cgitb


class WebManager:
    def __init__(self):
        cgitb.enable()
        self.headers = {}

    def addHeader(self, head, content):
        self.headers[head] = content

    def writeHeaders (self):
        for (k, v) in self.headers.items():
            print('%s: %s \r\n' % (k, v))

        print('\n')