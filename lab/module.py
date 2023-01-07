#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def foo(typ):
    def bar(spisok):
        if typ == list:
            return list(map(int, spisok.split()))
        return tuple(map(int, spisok.split()))

    return bar
