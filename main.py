import winsound
import time
from config import NOTES, DURATIONS

class PySinger():    
    A4 = 440 # Set base frequency.

    def __init__(self):
        return
    
    def read(self, file):
        with open(file) as f:
            musicString = f.read()
        f.close()
        return musicString

    def getFrequency(self, halfSteps):
        freq = self.A4 * ((2**(1/12)) ** halfSteps)
        return round(freq)

    def play(self, file):
        music = self.read(file).split(",")
        
        for i in range(len(music)):
            note = music[i]
            #print(note)
            
            if note == "_":
                time.sleep(1.25)
            else:
                if len(note) > 3:
                    # accidental
                    f = self.getFrequency(NOTES[note[:3]])
                    d = DURATIONS[note[3:]]
                else:
                    # natural
                    f = self.getFrequency(NOTES[note[:2]])
                    d = DURATIONS[note[2:]]
                
                winsound.Beep(f,d)