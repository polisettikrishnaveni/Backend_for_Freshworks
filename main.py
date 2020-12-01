import threading
from threading import*
import time

m={} #'m' is the dictionary in which we store data

#Error Message for key not present in the dictionary
def keynotpresent():
    print("ERROR: Given key does not exist in database. Please enter a valid key")

#for create operation
def Create(key,value,timetolive=0):
    if key in m:
        print("ERROR: This key name already exists") #error message1
    else:
        if(key.isalpha()):
            if len(m)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB
                if timetolive==0:
                    l=[value,timetolive]
                else:
                    l=[value,time.time()+timetolive]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    m[key]=l
            else:
                print("ERROR: Memory limit exceeded!! ")#error message2
        else:
            print("ERROR: Invalind key name!! key name must contain only alphabets")#error message3

#for read operation
def Read(key):
    if key not in m:
        keynotpresent()
    else:
        t=m[key]
        if t[1]!=0:
            if time.time()<t[1]: #comparing the present time with expiry time
                json=str(key)+":"+str(t[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return json
            else:
                print("ERROR: time-to-live of",key,"has expired") #error message5
        else:
            json=str(key)+":"+str(t[0])
            return json

#for delete operation
def Delete(key):
    if key not in m:
        keynotpresent()
    else:
        d=m[key]
        if d[1]!=0:
            if time.time()<d[1]: #comparing the current time with expiry time
                del m[key]
                print("key is successfully deleted")
            else:
                print("ERROR: time-to-live of",key,"has expired") #error message5
        else:
            del m[key]
            print("key is successfully deleted")

#Threading operations
t1=Thread(target=Read,args=(1,))
t1.start()
time.sleep(2)
t2=Thread(target=Delete,args=(3,)) 
t2.start()
time.sleep(4)
