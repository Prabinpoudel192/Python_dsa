



class ttb:
   def __init__(self,data,nodes):
      self.data=data
      self.nodes=nodes
      self.graph={}
      self.queue=[]
      self.visited=[]
      self.bfs=[]
      for i,j in enumerate(data):
          self.graph[i]=j

   def bfs_queue(self):
    
      try:
         root=int(input("Please choose the root node for the bfs traversal:\n"))
         self.queue.append(root)
         self.visited.append(root)
         while self.queue:       
           m=self.queue.pop(0)
           self.bfs.append(m)
           for i in self.graph[m]:
               if i not in self.visited:
                  self.queue.append(i)
                  self.visited.append(i)
         return self.bfs
      except Exception as e:
           print(f"{e}\n Operation Invalidated")
    
       

   
