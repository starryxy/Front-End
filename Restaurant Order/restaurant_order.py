#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 2019
"""

# format order item input
def formatItem(textLine) :
    # .strip() removes both leading and trailing spaces; optional
    textLine = textLine.lower().strip()
    # .split() splits words
    wordList = textLine.split()
    # .join() join words together with space as seperator
    textLine = " ".join(wordList)
    return textLine


# format quantity input
def formatQuantity(textLine) :
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = "".join(wordList)
    return textLine


price = dict([('egg', 0.99), ('bacon', 0.49), ('sausage', 1.49), ('hash brown', 1.19), ('toast', 0.79), ('coffee', 1.09), ('tea', 0.89)])

small = dict([('egg', 1), ('bacon', 2), ('sausage', 1), ('hash brown', 1), ('toast', 2)])
regular = dict([('egg', 2), ('bacon', 4), ('sausage', 2), ('hash brown', 1), ('toast', 2)])
big = dict([('egg', 3), ('bacon', 6), ('sausage', 3), ('hash brown', 2), ('toast', 4)])

price['small breakfast'] = sum(float(small[item]) * float(price[item]) for item in small)
price['regular breakfast'] = sum(float(regular[item]) * float(price[item]) for item in regular)
price['big breakfast'] = sum(float(big[item]) * float(price[item]) for item in big)

order = ""
quantity = ""
cost = 0
tax = 0
total = 0


while order != 'q':
    # prompt item request
    order = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    order = formatItem(order)
    if order == 'q':
        continue
    elif order not in price:
        print("Sorry, we don't have this item. Please enter again. ")
    else:
        # keep prompting quantity request until getting an int
        while True:
            quantity = input("Enter quantity: ")
            quantity = formatQuantity(quantity)
            if quantity.isnumeric():
                quantity = float(quantity)
                cost += price[order] * quantity
                break
            else :
                print("Sorry, we didn't get it. Please enter the quantity you'd like to order in number. ")
else:
    tax = cost * 0.13
    total = cost + tax
    print()
    print("Cost:  $", round(cost, 2))
    print("Tax:   $", round(tax, 2))
    print("Total: $", round(total, 2))
    print()
    print("Process finished with exit code 0")
