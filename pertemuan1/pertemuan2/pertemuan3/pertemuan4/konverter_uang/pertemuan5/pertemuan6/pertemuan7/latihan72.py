class Node:
    def __init__(self, plat):
        self.plat = plat
        self.Next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def tambahKendaraan(self, plat):
            new_node = Node(plat)

            if self.head is None:
                self.head = new_node
                return 
            
            temp = self.head
            while temp.Next:
                temp = temp.Next

            temp.Next = new_node

        def __init__(self, plat):
            temp = self.head

            if temp and temp.plat == plat:
                self.head
            
            
        