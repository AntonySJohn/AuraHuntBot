from telegram import *
from telegram.ext import *

class Questions:
    QUESTIONS = [
    {
        "text":"""Your entry is password protected. Solve the riddle below to get the three digit password to
ensure entry to the next level.

The three digits of the password is in ascending order

Three digit when multiplied, you will get 36

Three digit when added, you will get a number related to Trayodashi

The highest digit in the number must be unique.
        """,
        "image":"",
        "answer":"229"
    },
    {
        "text":"""Lets have fun with numbers again. Enter the required 11 digit number below.

The ‘perfect’ man is 160 ft.

First three numbers refer to the length of the outspread arms.

Next two numbers are the maximum width of the shoulder.

Next two number is the distance from elbow to tip of the hand

Next two number is the length of the hand

Next two numbers refer to the from below the chin to top of the head.
        """,
        "image":"",
        "answer":"16040401620"
    },
    {
        "text":"Solve the puzzle and identify the country",
        "image":"https://drive.google.com/uc?id=1wzyaJJB8B0BN7Cecd6Xg2rbETMwQ76L3&export=download",
        "answer":"australia"
    },
    {
        "text":"Figure it out",
        "image":"https://drive.google.com/uc?id=1fqgcw7bccFkHhOjBohDuCe87paQ6dxDo&export=download",
        "answer":"chariots of fire",
    },
    {
        "text":"""Your clue awaits in the folios of the work done by a famous author who is buried in a cemetery in Amiens which has a text 'LA MENDICITÉ EST DÉFENDUE DANS LE DÉPART DE LA SOMME' on its entry gate.

Pg3-P1-W10

Pg62-P1-W33

Pg5-P2-W17

Pg94-P1-W3

Pg112-P1-W10

Pg4-P2-W42

Pg16-P1-W4

Pg175-P2-W17

Pg3-P1-W9

Pg25-P1-W13

Pg69-P1-W16
        """,
        "image":"",
        "answer":"666"
    },
    {
        "text":"Here is your final challenge!",
        "image":"https://drive.google.com/uc?id=1qikl5tkFWXOH94dLRSO306-GccXSBPg4&export=download",
        "answer":"elizabeth"
    }
    ]

    def __init__(self,questionNumber):
        self.question = self.QUESTIONS[questionNumber]