from threading import Timer

def twoArgs(arg1,arg2):
    print (arg1)
    print (arg2)
    print ("")

def nArgs(*args):
    for each in args:
        print (each)

#arguments: 
#how long to wait (in seconds), 
#what function to call, 
#what gets passed in
r = Timer(25.0, twoArgs, ("1","2"))
s = Timer(2.0, nArgs, ("3","4","5"))

r.start()
s.start()