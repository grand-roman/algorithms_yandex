#https://contest.yandex.ru/contest/18168/run-report/36875797/

class Node:  
    def __init__(self, value, next=None):  
        self.value = value  
        self.next = next  
    def __repr__(self):  
        return self.value
        
def hasCycle(head):

    if head == None:
        return False

    one = head
    two = head

    while two.next != None and two.next.next != None:
        one = one.next
        two = two.next.next
        if one == two:
            return True
      
    return False
