# import sys
# import os
# sys.path.append(os.getcwd())

def validateUser(username, password):
        usersDict = createDictionary()
        if username in  usersDict.keys():
            if usersDict[username]== password:
                return  True
        return False

def createDictionary():
    usersDict = {}
    with open("usersFile.txt", "r") as usersFile:
        fileStr = usersFile.read()
        arr = fileStr.split('\n')
        for member in arr:
            smallArr = member.split(',')
            usersDict[smallArr[0]] = smallArr[1]
        return usersDict