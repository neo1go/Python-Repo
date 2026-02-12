from PIL import Image, ImageTk # pip install pillow und eventuell von python 8.14 auf 8.11 wechseln mittels str+shift+p
import random
import tkinter as tk

# =========================
# Kartendeck
# =========================

def create_card_deck(image_path: str) -> list[dict]:
    image = Image.open(image_path)
    image_width, image_height = image.size

    rows = 4
    columns = 8

    card_width = int(image_width / columns)
    card_height = int(image_height / rows)

    bilder = ["7", "8", "9", "10", "Bube", "Dame", "König", "As"]
    farben = ["Herz", "Karo", "Pik", "Kreuz"]
    werte = [7, 8, 9, 10, 10, 10, 10, 11]

    deck = []

    for row_index, farbe in enumerate(farben):
        for col_index, bild in enumerate(bilder):
            deck.append({
                "bild": bild,
                "farbe": farbe,
                "value": werte[col_index],
                "x": col_index * card_width,
                "y": row_index * card_height,
                "width": card_width,
                "height": card_height
            })

    return deck

# =========================
# Player
# =========================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.punkte = 0
        self.karten = []

# =========================
# Spielzustand & globale Variablen
# =========================

IMAGE_PATH = "karten_k.png"

spieler1 = Player("Frank")
spieler2 = Player("Dieter")
aktueller_spieler = spieler1
deck = []

karten_labels = []  # <- alle angezeigten Karten hier speichern
sprite = None       # wird später geladen

# =========================
# GUI Hilfsfunktion
# =========================

def show_last_card(spieler: Player, x: int, y: int):
    if not spieler.karten:
        return

    karte = spieler.karten[-1]

    box = (
        karte["x"],
        karte["y"],
        karte["x"] + karte["width"],
        karte["y"] + karte["height"]
    )

    img = sprite.crop(box)
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=tk_img)
    label.image = tk_img
    label.place(x=x, y=y)

    # Label in globale Liste aufnehmen
    karten_labels.append(label)

# =========================
# Spiel-Logik
# =========================

def neues_spiel():
    global deck, aktueller_spieler

    deck = create_card_deck(IMAGE_PATH)
    random.shuffle(deck)

    spieler1.karten.clear()
    spieler2.karten.clear()
    spieler1.punkte = 0
    spieler2.punkte = 0

    # Punkte zurücksetzen
    punkte1_label.config(text="Punkte: 0")
    punkte2_label.config(text="Punkte: 0")
    status_label.config(text="")

    # Karten-Labels löschen
    for label in karten_labels:
        label.destroy()
    karten_labels.clear()

    aktueller_spieler = spieler1
    btn_ziehen.config(state=tk.NORMAL)

def draw_card():
    global aktueller_spieler

    if not deck:
        spiel_beenden()
        return

    karte = deck.pop(0)
    aktueller_spieler.karten.append(karte)
    aktueller_spieler.punkte += karte["value"]

    if aktueller_spieler == spieler1:
        show_last_card(spieler1, x=100, y=80)
        punkte1_label.config(text=f"Punkte: {spieler1.punkte}")
        aktueller_spieler = spieler2
    else:
        show_last_card(spieler2, x=500, y=80)
        punkte2_label.config(text=f"Punkte: {spieler2.punkte}")
        aktueller_spieler = spieler1

def spiel_beenden():
    btn_ziehen.config(state=tk.DISABLED)

    # Gewinner bestimmen
    if spieler1.punkte > spieler2.punkte:
        status_label.config(text=f"Gewinner: {spieler1.name}")
    elif spieler2.punkte > spieler1.punkte:
        status_label.config(text=f"Gewinner: {spieler2.name}")
    else:
        status_label.config(text="Unentschieden")

    # Karten-Labels entfernen
    for label in karten_labels:
        label.destroy()
    karten_labels.clear()

# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Kartenspiel")
root.geometry("750x450")
root.resizable(False, False)

sprite = Image.open(IMAGE_PATH)

# Überschriften
tk.Label(root, text=f"{spieler1.name}").place(x=125, y=20)
tk.Label(root, text=f"{spieler2.name}").place(x=525, y=20)

# Punkte
punkte1_label = tk.Label(root, text="Punkte: 0")
punkte1_label.place(x=110, y=310)

punkte2_label = tk.Label(root, text="Punkte: 0")
punkte2_label.place(x=510, y=310)

# Status / Gewinner
status_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
status_label.place(x=270, y=300)

# Buttons
btn_ziehen = tk.Button(root, text="Nächste Karte", command=draw_card)
btn_ziehen.place(x=300, y=150)

btn_neu = tk.Button(root, text="Nochmal spielen", command=neues_spiel)
btn_neu.place(x=290, y=390)

btn_ende = tk.Button(root, text="Ende", command=root.destroy)
btn_ende.place(x=650, y=390)

# Spiel initial starten
neues_spiel()
root.mainloop()
