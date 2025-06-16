# Leetcode Nr.3
# Hier geht es um das Wiederauftauchen des selben Buchstaben und das Erweitern eines Fensters mit 2 Pointern. Wenn auf ein Char-Duplikat getroffen wird, muß es an erster Stelle
# im aktuellen Fenster stehen. Somit wird bei Erkennen eines Duplikates mittels eines Sets die Länge ermittelt und dann der linke Pointer um eins nach rechts verschoben.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {} # ein Dict das dann alle Chars und deren Char-Indexe speichert
        left = 0
        max_length = 0
        for right in range(len(s)): # rechter Pointer wird bewegt
            current_char = s[right]   # Speichern des chars an Stelle 'right' aus dem String 's' 
            if current_char in char_index and char_index[current_char] >= left:  # durch das '>= left' wird geschaut, ob der char in dem aktuellen Fenster liegt.
                left = char_index[current_char] + 1  # wenn der Wert im aktuellen Fenster doppelt ist, wird der linke Pointer um eins nach rechts verschoben.
            char_index[current_char] = right # Char-Index an Stelle des rechten Pointers wird in das Set eingetragen und ersetzt den alten Wert, der vorher für diesen char 
            # existierte. Also in unserem Beispiel war a: 0 und nun treffen wir auf ein Duplikat, also wird a:3 und der linke Pointer wird um eins nach rechts verschoben.
            # Somit steht dann in char_index {b:1,c:2,a:3} -> dies entspricht der Länge max(3,  und dann 3 - 1 + 1)    {plus 1 wegen 0 Index}. 
            max_length = max(max_length, right - left + 1)

        return max_length
        
      
      
        
s = ("abcabcbb")
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
