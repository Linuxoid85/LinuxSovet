#!/usr/bin/python3
# Скрипт для автоматизированного создания
# страниц на сайте.

import os
import sys
import time
import argparse
import configparser

config = configparser.ConfigParser()
config.read("./config.ini")

parser = argparse.ArgumentParser(
    description="Утилита для автоматизированного создания страниц"
)

parser.add_argument(
    "--page", "-p", type=str, help="Страница, которую требуется создать", required=True
)

parser.add_argument(
    "--header", "-H", type=str, help="Заголовок страницы", required=True
)

parser.add_argument(
    "--type", "-t", type=str, help="Тип", choices=['article', 'gallery']
)

args = parser.parse_args()
PAGE = args.page

def write(message, file):
    file = file + ".md"

    f = open(file, "a")
    f.write(message)
    f.close()

def init():
    for page in PAGE, PAGE+'.md':
        if os.path.isfile(page):
            os.remove(page)
    
    AUTHOR = config.get("Base", "author")
    DATE   = time.ctime()
    HEADER = args.header
    
    write(f"# {HEADER}\n", PAGE)

    if args.type:
        if args.type == "article":
            write("\n[Статьи]() > []\n", PAGE)

        elif args.type == "gallery":
            write("\n[Галерея]()\n", PAGE)
            write("\n<a href='pic/*.png'><img src='pic/*.png' width='455' height='256'></a>\n", PAGE)
        else:
            write("\n[На главную](/LinuxSovet/README.md)", PAGE)
    else:
        write("\n[Статьи]() > []\n", PAGE)

    write(f"\n<pre>\n<strong>Автор:</strong> {AUTHOR}\n", PAGE)
    write(f"<strong>Дата написания:</strong> {time.ctime()}\n<pre>\n\n", PAGE)

init()