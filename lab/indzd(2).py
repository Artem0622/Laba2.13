#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
from packet.add import add
from packet.help_1 import help_d
from packet.list_p import list_p
from packet.select import select

if __name__ == '__main__':
    # Список студентов.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            students = add(students)
        elif command == 'list':
            list_p(students)
        elif command == 'select':
            select(command, students)
        elif command == 'help':
            help_d()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)