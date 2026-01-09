
edges=[]
nodes=set()
a_l=[]
inf=10**10
visited=[]
dist=[]
def insert():
    global a_l
    a_l=[[] for _ in range(max(nodes)+1)]
    for n1,n2,wt in edges:
       a_l[n1].append((n2,wt))
       a_l[n2].append((n1,wt))
def display(root):
  global visited,dist,a_l
  visited=[False for _ in range(len(a_l))]
  dist=[inf for _ in range(len(a_l))]
  dist[root]=0
 
  
  for _ in range(len(a_l)):
      u=-1
      min=inf 
      for i in range(len(a_l)):
         if not visited[i] and dist[i]<min:
              min=dist[i]
              u=i
      if u==-1:
         break
         
            
      visited[u]=True
      for v,wt in a_l[u]:
          if dist[u]+wt<dist[v] and not visited[v]:
            dist[v]=dist[u]+wt
                
  print(f"Shortest path from {root} are:\n")
           
       
while True:
        try:
          inp=int(input("1 for insert,2 for shortest path and 0 for exit:\n"))
        except Exception as e:
          print(f"{e},Please provide valid input.")
          continue
        if inp==1:
            while True:
              try:
                 val=input("Provide input in node1,node2,weight format(q to quit):\n")
                 if val.lower()=='q':
                       break
                 else:
                  n1,n2,wt=map(int,val.split(","))
                  nodes.update([n1,n2])
                  edges.append((n1,n2,wt))
                  insert()        
              except Exception as e:
               print(f"\n{e},Error!! please provide valid input.")
               continue
        elif inp==2:
           while True:
                try:
                  inp1=int(input("Please enter the root nodes to start:"))
                except Exception as e:
                 print(f"{e},Please enter the valid node")
                 continue
                if inp1 not in nodes:
                   print("No such node")
                   continue
              
                else:
                   display(inp1)  
                   for v,dis in enumerate(dist):
                    if inp1==v:
                       continue
                    else:
                      print(f"{v}-------------->{dis}") 
                break       
            
              
        elif inp==0:
            print("Qutting the program!! Bye!!!!")
            break
        else:
            print("Invalid input,provide valid input")
            continue
    