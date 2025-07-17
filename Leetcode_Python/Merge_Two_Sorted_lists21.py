# Leetcode 21
# 2 Linked Lists zusammenführen
# Die Besonderheit ist die Verkettung der linked Lists und somit die Knoten.
# Es werden die Referenzen einfach neu geschrieben, um dann euf den richtigen Wert zu zeigen und es wird in diesem Fall eine
# Dummy Linked List erzeugt, die dann bei 0 oder -1 starten muß, also einem Wert vor dem ersten Wert einer der beiden Vergleichslisten.
# Es wird mit next iteriert.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(-1)   # dies ist ein Node der als dummy noch vor den ersten Knoten gesetzt wird.
        current = dummy    # aktueller Wert
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
         
        current.next = list1 if list1 else list2   # wenn eine List kürzer als die andere ist.           
                    
        return dummy.next   # dummy.next ist somit der erste echte Wert in der Dummy Kette, welcher von uns eingetragen wurde.
        

        
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()

result = sol.mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" -> ")
    result = result.next