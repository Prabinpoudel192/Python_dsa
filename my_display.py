class show:
    def __init__(self,bfs,data,t_type):
     self.bfs=bfs  
     self.data=data
     self.t_type=t_type
     self.val=""
     if(t_type.lower()=="bfs"):
        self.val="Breadth First Search"
     else:
        self.val="Depth First Search"
    def show(self):
        print("###########################")
        print("Graph:")
        for i,j in enumerate(self.data):
           print(f"{i}------>{j}")
        print("###########################")
        print("===========================")
        print(f"The {self.val} result:")
        print("\n")
        for i,j in enumerate(self.bfs):
           if(i==len(self.bfs)-1):
              print(f"{j}")
           else:
              print(j,end="---->")
        print("===========================")   

