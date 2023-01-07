#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_p(list_stud):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Номер группы",
            "Успеваемость"
        )
    )
    print(line)
    # Вывести данные о всех студентах.
    for idx, worker in enumerate(list_stud, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('number', ''),
                ' '.join([str(x) for x in worker.get('marks', 0)])

            )
        )
    print(line)