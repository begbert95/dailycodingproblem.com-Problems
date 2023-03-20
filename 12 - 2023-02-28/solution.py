import time

def scheduler(f, n):
    #Divide by 1000 because sleep takes in seconds, but n is in milliseconds
    time.sleep(n / 1000)
    f()


def printCat():
    print("meow")

scheduler(printCat, 1000)