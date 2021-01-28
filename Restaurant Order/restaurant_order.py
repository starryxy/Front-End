#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 2019
"""

# format order input
def formatInput1(textLine) :
    # .strip() removes both leading and trailing spaces; optional
    textLine = textLine.lower().strip()
    # .split() splits words
    wordList = textLine.split()
    # .join() join words together with space as seperator
    textLine = " ".join(wordList)
    return textLine

# format quantity input
def formatInput2(textLine) :
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = "".join(wordList)
    return textLine


price = dict([('egg', 0.99), ('bacon', 0.49), ('sausage', 1.49), ('hash brown', 1.19), ('toast', 0.79), ('coffee', 1.09), ('tea', 0.89)])


order = ""
quantity = ""
cost = 0
tax = 0
total = 0


while order != 'q' :
    order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    order = formatInput1(order)
    if order in price:
        while True :
            quantity = input("Enter quantity: ")
            quantity = formatInput2(quantity)
            if quantity.isnumeric():
                quantity = float(quantity)
                cost = cost + price[order] * quantity
                break
            else :
                print("Sorry, we didn't get it. Please enter the quantity you'd like to order. ")
    elif order == 'small breakfast' :
        sb = dict([('egg', 1), ('bacon', 2), ('sausage', 1), ('hash brown', 1), ('toast', 2)])
        while True :
            quantity = input("Enter quantity: ")
            quantity = formatInput2(quantity)
            if quantity.isnumeric():
                quantity = float(quantity)
                cost = cost + sum(float(sb[i]) * float(price[i]) for i in sb) * quantity
                break
            else :
                print("Sorry, we didn't get it. Please enter the quantity you'd like to order. ")
    elif order == 'regular breakfast' :
        rb = dict([('egg', 2), ('bacon', 4), ('sausage', 2), ('hash brown', 1), ('toast', 2)])
        while True :
            quantity = input("Enter quantity: ")
            quantity = formatInput2(quantity)
            if quantity.isnumeric():
                quantity = float(quantity)
                cost = cost + sum(float(rb[i]) * float(price[i]) for i in rb) * quantity
                break
            else :
                print("Sorry, we didn't get it. Please enter the quantity you'd like to order. ")
    elif order == 'big breakfast' :
        bb = dict([('egg', 3), ('bacon', 6), ('sausage', 3), ('hash brown', 2), ('toast', 4)])
        while True :
            quantity = input("Enter quantity: ")
            quantity = formatInput2(quantity)
            if quantity.isnumeric():
                quantity = float(quantity)
                cost = cost + sum(float(bb[i]) * float(price[i]) for i in bb) * quantity
                break
            else :
                print("Sorry, we didn't get it. Please enter the quantity you'd like to order. ")
    elif order == 'q' :
        continue
    else :
        print("Sorry, we don't have this. Please enter again. ")
else :
    tax = cost * 0.13
    total = cost + tax
    print()
    print("Cost: ", round(cost, 2))
    print("Tax: ", round(tax, 2))
    print("Total: ", round(total, 2))
    print()
    print("Process finished with exit code 0")
