from abc import ABC, abstractmethod
from datetime import datetime


class WriteFile(ABC):
    
    @abstractmethod
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename
        
    def write_line(self, text):
        with open(self.filename, 'w') as fh:  # a steht für append, es wird nur angehangen. Mit 'w' wird geschrieben bzw überschrieben.(write)
            fh.write(text + '\n')
        print(f'(geschrieben in {self.filename}): {text}')
 
        
class DelimFile(WriteFile):   # der delimiter ist das Trennzeichen für die Einträge wie z.B. bei csv Dateien.
    
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename) # Achtung, es wird der originale Konstruktor angesprochen und überschrieben (ACHTUNG Overriding).
        self.delim = delim
    
    def write(self, this_list):  # als Beispiel wenn immer die Datei erweitert wird. # overriding
        line = self.delim.join(this_list)
        self.write_line(line)  # write_line aus Superklasse wird aufgerufen
        

class LogFile(WriteFile):
    
    def write(self, this_line):   # overriding
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M:%S')
        self.write_line('{0}   {1}'.format(date_str, this_line))    # write_line aus Superklasse wird aufgerufen.
    
    
    # overloading wird es nur genannt, wenn es in der gleichen Klasse stattfindet. Ansonsten ist es overriding.