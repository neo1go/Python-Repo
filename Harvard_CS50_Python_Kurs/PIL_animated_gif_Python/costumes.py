# a gif is a combination of a number or images that are shown in succesion , sometimes in a loop.
import sys

from PIL import Image       # pip install pillow  # Pill läuft nicht wegen einer zu neuen Version, die noch nicht mit PIL kompatibel ist. 


images = []   # die Liste, auf die dann zugegriffen wird


for arg in sys.argv[1:]:# hier werden die Bilder von außen eingefügt und dnn nach dem Öffnen in image gespeichert und als letztes in images gespeichert.
    image = Image.open(arg)
    images.append(image)


images[0].save(      # hier werden die Bilder angehangen und gespeichert
    "costumes.gif", save_all=True, append_images=images[1:], duration=200, loop=0
)

# code zum Ausführen wenn dann die Version PIP unterstützt :   python costumes.py costume1.gif costume2.gif costume1.gif costume3,gif
# und anschließend :  code costumes.py