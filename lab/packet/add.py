#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(list_stud):
    # Запросить данные о студентах.
    name = input("Фамилия и инициалы? ")
    number = input("Номер группы? ")
    marks = list(map(int, input("Успеваемость").split()))
    # Создать словарь.
    student = {
        'name': name,
        'number': number,
        'marks': marks,
    }
    # Добавить словарь в список.
    list_stud.append(student)
    # Отсортировать список в алфавитном порядке.
    if len(list_stud) > 1:
        list_stud.sort(key=lambda item: item.get('name', ''))
    return list_stud