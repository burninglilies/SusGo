from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
board = []
actions = ['Use Reusable Bag for Groceries', 'Take a short shower', 'Use a travel water bottle', 'Refill a water bottle', 'Go to a public park', 'Clean up a public park', 'Clean the Beach', 'Clean the Beach', 'Clean the Beach', 'Clean the Beach', 'Repost this Week\'s Bingo!',
           'Go to a public park', 'Use a Travel Water Bottle', 'Free Space', 'Clean up a public park', 'Use Reusable Bag for Groceries', 'Take the Bus', 'Take the Bus', 'Take the Bus', 'Take the Bus', 'Take the Bus', 'Thrifting', 'Thrifting', 'Thrifting', 'Thrifting', 'Thrifting']


def setBoard():
    row0 = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []

    for x in range(len(actions)):

        if x < 5:
            row0.append(actions[x])
        if x >= 5 and x < 10:
            row1.append(actions[x])
        if x > 10 and x < 15:
            row2.append(actions[x])
        if x > 15 and x < 20:
            row3.append(actions[x])
        if x > 20 and x < 25:
            row4.append(actions[x])

    board.append(row0)
    board.append(row1)
    board.append(row2)
    board.append(row3)
    board.append(row4)
