#!/usr/bin/python3

import os

print("Ваш PATH:")
print(os.environ.get('PATH'))

directory = os.environ.get('PWD')
print("Вы находитесь в директории {}".format(directory))
