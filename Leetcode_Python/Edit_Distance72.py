# Leetcode 72
# es soll die minimale Anzahl an Operationen herausgefunden werden, um
# einen String in einen anderen String umzuwandeln,
# entweder mit insertion, deletion oder substitution. Jeder dieser Operationen zählt als eine einzelene Operation
# und bei mehreren gleichen Buchstaben wird jedesmal gezählt.
# Es wird mit memoization in einer 2d Matrix gearbeitet.
# Die Matrix muß um einen Eintrag größer sein da auch ein leerer String in Frage kommen kann
# und bei gleichen Buchstaben (also keine Operation) wird einfach der Nullwert der ersten Koordinate übernommen.
# Der Trick:
# Wenn die Buchstaben nicht gleich sind, dann werden für das aktuelle Feld die
# vorherigen angrenzenden Werte (links, oben u. oben links) verglichen und der niedrigste Wert +1 genommen und an diese Stelle gesetzt.
# Die Länge der Wörter sind für die Erstellung sehr wichtig, genauso wie die 0 Zeile und 0 Spalte, die 
# von 0 bis Ende des Strings die Werte eingtragen und somit die Basiswerte bilden.
# Z.B. bei den Strings "froh" und "hoh" hat man bei "froh" die Werte 0,1,2,3 und bei "hoh" als Spalte die Werte 0,1,2 in der Zeile und Spalte. 
# Und wenn sich im Koordinatensystem die Buchstaben gleichen, wird der Wert aus der ersten Koordinate dort eingetragen, nämlich 0.

# Anwendungseinsatz sind z.B.string Vergleiche um die Strings zu finden, die sich am Ähnlichsten sind.

class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
                              # n Spalten           m Zeilen
        costDP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # nur um die erste Zeile(0) und Spalte(0) mit den logischen aufsteigenden Werten zu befüllen.
        # Diese sind die Basiswerte, an die sich alle anderen Additionen in der Matrix halten. 
        # es wird mit m angefangen weil bei der Erstellung die Schleifen verschachtelt sind.
        for i in range(m + 1):
            costDP[i][0] = i
        for j in range(n+1):
            costDP[0][j] = j
    
        # nun wird über die Matrix iteriert und populiert:
        for i in range(1, m + 1):   # word2
            for j in range(1, n + 1):
                if word1[j-1] == word2[i-1]:
                    costDP[i][j] = costDP[i-1][j-1]  # Nullwert setzen da keine Kosten entstehen.
                else:
                    # diese Koordinaten sind der Trick:
                    topleft = costDP[i-1][j-1]
                    top = costDP[i-1][j]
                    left = costDP[i][j-1]
                    
                    costDP[i][j] = min(topleft, min(top, left)) + 1  # populiert die Matrix nahand der vorherigen Werte.
        
        return costDP[m][n]   # der letzte Eintrag in der Wertetabelle zeigt die minimalen Operationen an.
    
word1 = "abcdef"
word2 = "azcde"
sol = Solution()
print(f"Niedrigste Anzahl an Operationen zum Angleichen: {sol.minDistance(word1, word2)}")