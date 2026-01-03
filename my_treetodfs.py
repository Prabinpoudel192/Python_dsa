



class ttd:
   def __init__(self,data,nodes):
      self.data=data
      self.nodes=nodes
      self.graph={}
      self.stack=[]
      self.visited=[]
      self.dfs=[]
      for i,j in enumerate(data):
          self.graph[i]=j

   def dfs_queue(self):
      
      try:
         root=int(input("Please choose the root node for the DFS traversal:\n"))
         self.stack.append(root)
         self.visited.append(root)
         while self.stack:       
           m=self.stack.pop()
           self.dfs.append(m)
           for i in self.graph[m]:
               if i not in self.visited:
                  self.stack.append(i)
                  self.visited.append(i)
         return self.dfs
      except Exception as e:
           print(f"{e}\n Operation Invalidated")
    
       

   
