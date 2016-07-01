"""
Title: Mega Projects List - Find Cost to Cover W x H Floor
Author: Mandeep Bhutani
Date: 06/20/2016
Problem: Calculate the total cost of tile it would take to cover a floor plan
of width and height, using a cost entered by the user.
"""
import locale
from decimal import Decimal, getcontext, ROUND_UP

room_width = Decimal(input('Enter the width of the room: '))
room_length = Decimal(input('Enter the length of the room: '))
cost_of_tile = Decimal(input('Enter the cost of the tile per unit: '))


def cost_to_cover_room(width, length, cost):
    locale.setlocale(locale.LC_ALL, '')
    getcontext().rounding = ROUND_UP
    total = Decimal(width * length * cost).quantize(Decimal('.01'), rounding=ROUND_UP)
    dollar_amount = locale.currency(total, grouping=True)
    return 'The total cost to cover the room with tile is {}.' .format(dollar_amount)

print(cost_to_cover_room(room_width, room_length, cost_of_tile))
