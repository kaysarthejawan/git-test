




class Node :
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self) -> None:
        self.start=None

    def show(self):
        if self.start==None:
            print("list is empty")
        else:
            temp=self.start
            while temp is not None:
                print(temp.data)
                temp=temp.next
    def remove_1st_one(self):
        if self.start==None:
            print('linked is empty')
        else:
            self.start=self.start.next
   # def remove_by_node(self,nodetoremove):
   #     nodetoremove.next=nodetoremove.next.next


    def remove_middile(self,indexnum):
        if indexnum==0:
            self.remove_1st_one()
        else:
            counter=0

            temp=self.start
        
            while counter!=indexnum-1:
                 temp=temp.next
                 counter+=1
            temp.next=temp.next.next
      
        print ('seccussfully removed')
    def insert_middle(self,newdata,afternode):
        newnode=Node(newdata)
        temp=self.start
        while temp.data != afternode:
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    def insert_by_index(self,newdata,indexnum):
        if indexnum==0:
            self.insert_1st(newdata)
        else:
            
            newnode=Node(newdata)
            counter=0
            temp=self.start
            while counter !=indexnum-1:
                temp=temp.next
                counter +=1
            newnode.next=temp.next
            temp.next=newnode
    def insert_1st(self,newdata):
        newnode=Node(newdata)
        temp=self.start
        newnode.next=temp
        self.start=newnode
    def removefrom_end(self,index_num_from_end):

        first=self.start  
        second=self.start
        counter=0
        while counter <=index_num_from_end:
            second=second.next
            counter+=1
        if second is None:
            self.remove_1st_one()
            return
        while second is not None:
            second=second.next
            first=first.next
        first.next=first.next.next

    def reverselinked(self):
        p1 = None
        p2=self.start
        
        while p2 != None:
            p3=p2.next
           
            p2.next=p1
            
            p1=p2
            p2=p3
        self.start=p1
    

    def insert_in_last(self,value):
        newnode=Node(value)
        if self.start==None:
            self.start=newnode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

mylist=linkedlist()
mylist.insert_in_last(10)
mylist.insert_in_last(12)
mylist.insert_in_last(100)
mylist.insert_in_last(106)
mylist.insert_in_last(107)
mylist.insert_in_last(1023)
mylist.insert_in_last(1067)

#mylist.remove_1st_one()
#mylist.show()
#mylist.remove_middile(6)
#mylist.insert_middle(234,10)
#mylist.insert_by_index(34,0)
#mylist.insert_1st(23)

#mylist.removefrom_end(7 )
#mylist.reverselinked()
#mylist.show() 
#print('end')                             
#insert from end 
#end of 1st linked list

class Node1:
    def __init__(self,data) :
        self.data=data
        self.next=None
class linkedlist1:
    def __init__(self) :
        self.start=None
    def show1(self):
        temp=self.start
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def insertlast(self,entered_data):
        newnode1=Node1(entered_data)
   

        if self.start==None:
            self.start=newnode1
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode1
mylist1=linkedlist1()
mylist1.insertlast(50)
mylist1.insertlast(60)
mylist1.insertlast(70)
mylist1.insertlast(80)
mylist1.insertlast(90)
mylist1.insertlast(100)

#mylist1.show1()
#print('end')
#
#ef merging():
#   temp=mylist.start
#   temp1=mylist1.start
#   p1=mylist.start
#   p2=mylist1.start
#   prev=None
#   while p1 is not None and p2 is not None:
#       if p1.data<p2.data:
#           prev=p1
#           p1=p1.next
#       else:
#           if prev is not None:
#               prev.next=p2
#           prev=p1
#           p2=p2.next
#           prev.next=p1   
#   if p1 is None:
#        prev.next=p2
#   if temp.data < temp1.data:
#       return temp


#merging()
#mylist.show()
def insertNodeAtPosition( data, position):
    newnode=Node(data)
    # Write your code here
    temp=mylist.start
    if position ==0:
        newnode.next=temp
        temp=newnode
        return
    
    counter=0
    while counter <=position :
        temp=temp.next
        counter +=1
    newnode.next=temp.next
    temp.next=newnode
    return newnode
insertNodeAtPosition(23,1)
mylist.show()

                
                









