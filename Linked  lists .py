class Element(object) :
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
        
    def append(self,new_element):
        current=self.head
        if(current):
               while current.next:
                   current=current.next
               current.next=new_element
        else:
            current.next=new_element
            
    def get_position(self,position):
        current=self.head
        counter=1
        if(position<1):
            return None
        while current and counter<=position:
            if(counter==position):
                return current
            current=current.next
            counter=counter+1
        return None
    def insert(self,new_element,position):
        current=self.head
        counter=1
        if(position>1):
            while current and counter<position:
                if(counter==position-1):
                    new_element.next=current.next
                    current.next=new_element
                current=current.next
                counter=counter+1
        elif(position==1):
            new_element.next=self.head
            self.head=new_element
    def delete(self,value):
        prev=None
        current=self.head
        while current.next and current.value!=value:
            prev=current
            current=current.next
        if(current.value==value):
            if prev:
                prev.next=current.next
            else:
                self.head=current.next
                

            
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)       
        