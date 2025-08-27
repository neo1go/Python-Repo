# das Observer Pattern besteht aus einem Subjekt, welches Änderungen seines Zustands an 
# mehrere Beobachter (Observer) weitergibt.

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None:
        pass

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

# Observer
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
