from django.db import models

# Create your models here.x
class avg:
    def __init__(self,data):
        self.data=data
        self.next=None
class node:
    def input(self,data):
        x=avg(data)
        if self.head==None:
            self.head=x
            return 
        temp=self.head
        while temp!=None:
            temp=temp.next
        temp=avg(data)
    def sum(self,x):
        k=0
        temp=self.head
        while temp:
            k+=temp.data
            p+=1
            temp=temp.next
        return k//p
            
        
            


