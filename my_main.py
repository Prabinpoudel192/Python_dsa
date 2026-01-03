
import my_graphtotree as mg
import my_treetobfs as mt
import my_display as dis
import my_treetodfs as md

edges=[]
data=[]
nodes=set()
bdfs=[]
if __name__=="__main__":
 A=mg.gtt()
 while True:
    try:
      a=int(input("1 for graph\n2 for bfs\n3 for dfs\n4 to clear\n0 for exit\nYour input:"))
      if a==1:
        edges,nodes,data=A.insert()
      elif a==2:
        if not data or not nodes:
            print("\nInvalid operation!! Create graph first")
            continue
        B=mt.ttb(data,nodes)
        bdfs=B.bfs_queue()
        C=dis.show(bdfs,data,"BFS")
        C.show()
      elif a==3:
          if not data or not nodes:
            print("\nInvalid operation!! Create graph first")
            continue
          D=md.ttd(data,nodes)
          bdfs=D.dfs_queue()
          C=dis.show(bdfs,data,"DFS")
          C.show()
      elif a==0:
        print("\nProgram is closing")
        break
      elif a==4:
        edges=[]
        data=[]
        nodes=set()
        bfs=[]
      else:
        continue
    except Exception as e:
     print(f"\n{e} Please enter the valid input.")
     continue