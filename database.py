from pyasn1.type.univ import Null
import pyrebase
from datetime import datetime

empty_data = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": ""}
"""
Connect to Firebase database
PS: Did not implement auth, you should probably do that
"""


def connectDatabase():
    config = {
        "apiKey": "",
        "authDomain": "ieee-aura-21-hunt.firebaseapp.com",
        "databaseURL": "https://ieee-aura-21-hunt-default-rtdb.firebaseio.com/",
        "storageBucket": "",
    }
    firebase = pyrebase.initialize_app(config)
    _db = firebase.database()
    return _db


"""
Get list of user data from database
"""


def getUsersData(_db):
    return list(_db.child("db").get().val().items())


"""
Adds new user to database if chatID is not found
"""


def addUser(chatID):
    db = connectDatabase()
    if not checkParticipant(db, chatID):
        data = {chatID: empty_data}
        db.child("db").push(data)


"""
Checks if participant is there in the list of user data retrieved
and returns boolean result
"""


def checkParticipant(_db, chatID):
    usersData = getUsersData(_db)
    if matchChatID(usersData, chatID) != Null:
        return True
    else:
        return False


"""
Searches the list of userData and returns a dict containing the userData
matching with chatID if found, else returns Null
"""


def matchChatID(_usersData, _chatID):
    for val in _usersData:
        userDict = list(val)[1]
        if (list(userDict.keys()))[0] == _chatID:
            return list(val)
    else:
        return Null


"""
Get current question for user using chatID
returns 0 if quest is completed
"""


def getUserQuestion(chatID):
    db = connectDatabase()
    usersData = getUsersData(db)
    user = matchChatID(usersData, chatID)[1]
    questionList = list(user.values())[0]
    for i in range(1, 7):
        if not questionList[i]:
            return i
    else:
        return 0


"""
Updating the database with timestamp of answering a question
"""


def updateAnswer(chatID, questionNumber):
    db = connectDatabase()
    usersData = getUsersData(db)
    firebaseTimestamp = matchChatID(usersData, chatID)[0]
    db.child("db").child(firebaseTimestamp).child(chatID).update(
        {str(questionNumber): datetime.now().strftime("%H:%M:%S")}
    )
