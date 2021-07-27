class tale:
    def __init__(self):
        self.head = None
        self.bottom = None
        self.len = 0

    def add(self,val):
        new_node = node(val)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.bottom
            
        self.bottom = new_node
        self.len += 1

        return self
    
    def remove(self):
        if self.len == 1:
            self.head = None
            self.bottom = None
            self.len = 0
            return self
        head = self.head
        actual = self.bottom
        while actual.next != head: 
            actual = actual.next 
        
        actual.next = None
        self.head = actual
        self.len -= 1


    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False
    def print_values(self):
        actual = self.bottom 
        while actual != None: 
            print(actual.value)
            actual = actual.next 

        return self

class node:
    def __init__(self,val):
        self.value = val
        self.next = None

cola = tale()
cola.add(1)
cola.add(2)
cola.add(3)
cola.add(4)
cola.print_values()
print("el largo:",cola.len)
print("---")
cola.remove()
cola.print_values()
print("el largo:",cola.len)
print("---")
cola.remove()
cola.print_values()
print("el largo:",cola.len)
print("---")
cola.remove()
cola.print_values()
print("el largo:",cola.len)
print("---")
cola.remove()
cola.print_values()
print("el largo:",cola.len)
