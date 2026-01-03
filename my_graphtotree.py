
class gtt:
    
    def __init__(self):
       self.lst=[]
       self.nodes=set()
       self.data=[]
    def insert(self):
        while True:
          try:
           a=input("Please enter the node('q' to quit):")
           if a.lower()=='q':
              break
           else:
             b,c=map(int,a.split(','))
             self.lst.append((b,c))
             
             for x,y in self.lst:
                 self.nodes.add(x)
                 self.nodes.add(y)
             
             self.data=[[] for _ in range(max(self.nodes)+1)]
             
             for x,y in self.lst:
                self.data[x].append(y)
                self.data[y].append(x)
          except Exception as e:
            print(f"{e} Please enter the valid value")
            continue
        return self.lst,self.nodes,self.data
 
