class Scheibe:
    def __init__(self, groesse: int, farbe: tuple):
        self.groesse = groesse
        self.farbe = farbe
   
ganz_klein = Scheibe(1,(220, 50, 50))     
klein = Scheibe(2,(50, 100, 220))
mittel = Scheibe(3,(50, 180, 80))
gross = Scheibe(4,(230, 180, 40))
ganz_gross = Scheibe(5,(160, 70, 200))