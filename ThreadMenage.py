import threading

class libThread(threading.Thread):

    def __init__(self,recievedFunction ):
        threading.Thread.__init__(self)
        self.__recievedFunction = recievedFunction

    def run(self):
        self.__recievedFunction()
      
