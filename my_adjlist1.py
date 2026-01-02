
import numpy as np
lst=[]
data=[]
nodes=set()
def add():
    while True:
      try:
      
          b=input("Please enter the edges:")
          c,d=map(int,b.split(','))
          lst.append((c,d))
          break
      except Exception as e:
       print (e)
       print("That wasn't the valid edges")
def remove():
    val=input("Please enter the edge to remove it from the edges:")
    try:
        e,f=map(int,val.split(','))
        
        if (e,f) in lst:
            lst.remove((e,f))
        if (f,e) in lst:
             lst.remove((f,e))
             
            
    except Exception as e:
        print(e)
        print("Invalid Edge")

def display():  
    global data
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            nodes.add(lst[i][j])
    data=[[] for _ in range(max(nodes)+1)]
    for x,y in lst:
       data[x].append(y)
       data[y].append(x)
    for i in range(len(data)):
        print(f"{i}-------------->{data[i]}")    

while True:
    try:
       a=int(input("1 to add edges,2 to display 3 to remove edge and 0 to quit:\n"))
    except Exception as e:
        print(e)
        print("Please enter the valid input")
    if a==1:
        add()
        display()
    elif a==2:
        display()
    elif a==3:
        remove()
        display()

    else:
        print("Bye!!!!!! The program is closing.")
        break


