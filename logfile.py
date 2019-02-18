from time import gmtime, strftime

def reportToLog(situation):
    with open("liberary.log", "a") as usersFile:
        string = situation + ': ' + strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + '\n'
        usersFile.write(string  )


