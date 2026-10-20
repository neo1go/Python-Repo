
from scheibe import ganz_gross, gross, mittel, klein, ganz_klein
from turm import Turm
from darstellung import Darstellung
from hanoi_solver import verschiebe
import pygame


turm_a = Turm("A")  # jeder Turm hat eine eigene Liste scheiben mit Scheiben
turm_b = Turm("B")
turm_c = Turm("C")


# Startturm (links größte Scheibe)
turm_a.scheiben = [ganz_gross, gross, mittel, klein, ganz_klein]

darstellung = Darstellung()

# Anfangszustand anzeigen
darstellung.zeichne(turm_a, turm_b, turm_c)
pygame.time.delay(1000)

# Nach jedem Zug die Darstellung aktualisieren
def aktualisiere():
    darstellung.animations_schritt(turm_a, turm_b, turm_c)

verschiebe(
    len(turm_a.scheiben),   # Anzahl der Scheiben kann variieren
    turm_a,
    turm_c,
    turm_b,
    aktualisiere  # Besonderheit, es wird die Funktion direkt übergeben ohne sie direkt auszuführen
)

# Endzustand anzeigen und Fenster offen halten
darstellung.starten(turm_a, turm_b, turm_c)
