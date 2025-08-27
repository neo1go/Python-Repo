# das Observer Pattern besteht aus einem Subjekt, welches Änderungen seines Zustands an 
# mehrere Beobachter (Observer) weitergibt.

from abc import ABC, abstractmethod
from typing import List, Protocol  # wird dann verwendet, wenn man nur 3 Punkte nutzt und damit ein Interface definieren will anstatt abstrakter Methoden. 
                                   # Es wird von Protocol geerbt. Alle gleichen Methodensignaturen gelten dann als verwandt (polymorph) 

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass
    """
    die 2te Variante ohne abc Import sind drei Punkte anstatt des pass Begriffs und natürlich ohne @abstractmethod, dafür aber mit der Vererbung von Protocol.
    Protocol ist dafür gedacht,dass, sobald eine Klasse eine identische Methode nutzt, die vorher schon erstellt wurde, dann gilt diese als kompatibel und somit polymorph.
    Man kann theoretisch die Observer ohne den Verweis zu Observer nutzen wenn man Protocol nutzt und durch eine identische Methodendeklaration wird der Observer erkannt.
    """
    
# Subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None  # Zustand

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)

    def set_temperature(self, new_temp: float):
        if new_temp != self._temperature:  # nur wenn sich was ändert
            self._temperature = new_temp
            self.notify()

    def notify(self):
        for obs in self._observers:
            obs.update(self._temperature)




# Observer  (wenn man die Protocol Klasse nutzen würde, könnte man den Observer weglassen da damit definiert wird, dass identische Methodensignaturen als verwandt gelten, 
# also hier in diesem Fall die update Methode, die ja alle Observer besitzen.)

class PhoneDisplay(Observer):
    def update(self, temperature: float):
        print(f"[Phone] Neue Temperatur: {temperature}°C")


class LEDDisplay(Observer):
    def update(self, temperature: float):
        print(f"[LED] Neue Temperatur: {temperature}°C")






# --- Nutzung ---
station = WeatherStation()
phone = PhoneDisplay()
led = LEDDisplay()

station.subscribe(phone)
station.subscribe(led)

station.set_temperature(20.0)  # löst notify() aus
station.set_temperature(20.0)  # keine Änderung → kein notify
station.set_temperature(22.5)  # Änderung → notify()

station.unsubscribe(phone)   
