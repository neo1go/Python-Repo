# Pyhton Alarm Clock
import time # dadurch kann man die Zeit sekundenweise anzeigen
import datetime  # mit diesem Modul kann man eine String Repräsentation der Zeit anzeigen lassen
import pygame
import threading
import msvcrt  # prüft nicht-blockierend, ob eine Taste gedrückt wurde



def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
 
 
def wait_for_user_stop():
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"[ALARM] Aktuelle Uhrzeit: {current_time}")
        
        if now.second %10 == 0:
            print("WAKE UP! 😴")
            
        time.sleep(1)
        
        if msvcrt.kbhit():
            input("Drücke ENTER um den Alarm zu stoppen.")
            pygame.mixer.music.stop()        #erst bei einem User-Input wird die Musik gestoppt und der boolean is_running auf false gesetzt.
            break
   

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    is_running = True
    sound_file = "Spaceship Alarm.mp3"
   
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Uhrzeit {current_time}")
        time.sleep(1)
        
        if current_time == alarm_time:
            print("WAKE UP! 😴")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            # Startet neuen Thread, der nur auf die Benutzereingabe wartet, während der Hauptthread mit dem Alarm weiterläuft.
            input_thread = threading.Thread(target=wait_for_user_stop)  # hier wird die Methode referenziert, die gestartet werden soll.
            input_thread.start()
            
                
            is_running = False
            
