#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(command_d, list_stud):
    # Инициализировать счётчик
    count = 0
    # Проверить студентов хотя бы на одну оценку.
    for student in list_stud:
        if 2 in student.get('marks', []):
            count -= 1
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №', student.get('number', ''))
            )
            # Если счётчик равен 0, то оценки не найдены.
    if count == 0:
        print('Таких студентов нет')