#!/usr/bin/env python
# -*- coding: utf-8 -*-
# WOPR (https://www.github.com/R3nt0n/wopr)
# R3nt0n (https://www.github.com/R3nt0n)

import time
import os

from asks import *


###############################################################################
def clear():
    os.system(['clear', 'cls'][os.name == 'nt'])


###############################################################################
def wopr(texto, ans, ask, ansCondition, saltosLinea, error):

    if ans.find(ansCondition) != -1:
            texto = texto + saltosLinea + ans + saltosLinea
            for i in ask:
                clear()
                texto += i
                print texto
                time.sleep(0.1)
            return texto

    while ans.find(ansCondition) == -1:
        if ans.find(ansCondition) == -1:
            texto = texto + saltosLinea + ans + saltosLinea
            for i in error:
                clear()
                texto += i
                print texto
                time.sleep(0.1)
            ans = raw_input('\n\n')

        if ans.find(ansCondition) != -1:
            texto = texto + saltosLinea + ans + saltosLinea
            for i in ask:
                clear()
                texto += i
                print texto
                time.sleep(0.1)
            return texto


###############################################################################
def chooseTarget(texto):
    clear()
    ans6 = raw_input(texto)

    if ans6 == '1' or ans6 == '2':
        clear()
        texto = wopr('', '', ask10, '', '', error)
        texto = wopr(texto, '', ask11, '', '', error)
        ans7 = raw_input('')
        ans7 = ans7.upper()
        clear()
        time.sleep(3)
        lon = len(ans7)
        cont = 0
        target = []
        while cont < lon:
            target.append(ans7[cont])
            cont = cont + 1
        texto = wopr('', '', ask12 + target, '', '', error)
        time.sleep(10)

    elif ans6 != '1' or ans6 != '2':
        print '\n       ERROR. CHOOSE 1 OR 2.'
        time.sleep(3)
        chooseTarget(texto)


###############################################################################
def logOn():
    texto = ''
    for i in logonSpell:
        clear()
        texto += i
        print texto
        time.sleep(0.1)
    clear()
    login = raw_input('LOGON: ')
    if login == 'Joshua':

        texto = ''
        for i in ask1:
            clear()
            texto += i
            print texto
            time.sleep(0.1)

        ans1 = raw_input('\n\n')
        texto = wopr(texto, ans1, ask2, 'Hello', '\n\n\n', error)

        ans2 = raw_input('\n\n')
        texto = wopr(texto, ans2, ask3, 'Fine', '\n\n\n', error)

        ans3 = raw_input('\n\n')
        texto = wopr(texto, ans3, ask4, 'mistakes', '\n\n\n', error)

        ans4 = raw_input('\n\n')
        texto = wopr(texto, ans4, ask5, 'Global Thermonuclear War', '\n\n\n', error)

        ans5 = raw_input('\n\n')
        texto = wopr(texto, ans5, ask6, 'Later', '\n\n\n', error)

        time.sleep(2.5)
        clear()
        printMap()

        texto = mapPrinted
        time.sleep(1)

        texto = wopr(texto, '', ask7, '', '', error)
        texto = wopr(texto, '', ask8, '', '\n', error)
        texto = wopr(texto, '', ask9, '', '\n', error)

        chooseTarget(texto)

    elif login != 'Joshua':
        print 'INCORRECT LOGON.'
        time.sleep(2)
        clear()
        logOn()


###############################################################################

logOn()
