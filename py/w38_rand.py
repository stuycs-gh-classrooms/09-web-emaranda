#!/usr/bin/python3
print('Content-type: text/html\n')

import random
randnum = random.random()
print('hello there world :D')
print(randnum)

def make_html_list(data):
    items = list(map(lambda a: '<li>' + str(a) + '</li>', data))
    full_items = '\n'.join(items)
    final = '<ul>' + '\n' + full_items + '\n' + '</ul>'
    return final

print(make_html_list([90, 99, 97, 89]))