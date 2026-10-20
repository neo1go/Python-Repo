

def verschiebe(anzahl, start, ziel, mitte, nach_zug=None):
    if anzahl == 0:
        return

    verschiebe(anzahl - 1, start, mitte, ziel, nach_zug)

    scheibe = start.scheiben[-1]

    if not ziel.darf_ablegen(scheibe):
        raise ValueError("Ungültiger Zug!")

    start.scheiben.pop()
    ziel.scheiben.append(scheibe)

    if nach_zug is not None:
        nach_zug()

    verschiebe(anzahl - 1, mitte, ziel, start, nach_zug)
