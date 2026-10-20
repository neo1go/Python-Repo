# hier werde ich pygame importieren um die Grafik zu erstellen

import pygame

class Darstellung:
    def __init__(self, breite = 900, hoehe = 600): # Canvasgröße
        pygame.init()
        
        self.breite = breite
        self.hoehe = hoehe
        
        self.screen = pygame.display.set_mode(
            (self.breite, self.hoehe)
        )
        
        pygame.display.set_caption("Turm von Hanoi")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Farben als RGB-Werte
        self.hintergrund = (240, 240, 240)
        self.turm_farbe = (70, 70, 70)
        self.scheiben_farbe = (60, 130, 200)
        self.text_farbe = (30, 30, 30)

        self.turm_positionen = [200, 450, 700]
        self.boden_y = 380  # Länge des Stabes, oberer Punkt bleibt fix
        
        
    def zeichne_turm(self, x, name):
        # Vertikaler Stab
        pygame.draw.rect(
            self.screen,
            self.turm_farbe,
            (x - 5, 220, 10, self.boden_y - 220) # x ist linke Kante, 220 ist Oberkante
        )
         
        # Bodenplatte
        pygame.draw.rect(
            self.screen,
            self.turm_farbe,
            (x - 105, self.boden_y, 220, 12)  # 180 Breite der Bodenplatte
        )
        
        schrift = pygame.font.Font(None, 30)
        text = schrift.render(name, True, self.text_farbe)
        
        self.screen.blit(text, (x - 10, self.boden_y + 25))
    
    def zeichne_scheiben(self, turm, x):
        scheiben_hoehe = 25
        basis_y = self.boden_y
        
        for index, scheibe in enumerate(turm.scheiben):
            breite = scheibe.groesse * 40
            y = basis_y - (index + 1) * scheiben_hoehe
            
            pygame.draw.rect(
                self.screen,
                self.scheiben_farbe,
                (x - breite // 2, y, breite, scheiben_hoehe - 2),
                border_radius=4
            )

    def animations_schritt(self, turm_a, turm_b, turm_c):
        self.zeichne(turm_a, turm_b, turm_c)
        pygame.event.pump()
        pygame.time.delay(500)
    
    def zeichne(self, turm_a, turm_b, turm_c):
        self.screen.fill(self.hintergrund)

        tuerme = [
            (turm_a, self.turm_positionen[0]),
            (turm_b, self.turm_positionen[1]),
            (turm_c, self.turm_positionen[2])
        ]

        for turm, x in tuerme:
            self.zeichne_turm(x, turm.name)
            self.zeichne_scheiben(turm, x)

        pygame.display.flip()

    def starten(self, turm_a, turm_b, turm_c):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.zeichne(turm_a, turm_b, turm_c)

            self.clock.tick(60)

        pygame.quit()