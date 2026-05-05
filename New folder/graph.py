adj = [[0,1,0,1]
       ,[1,0,1,0]
       ,[0,1,0,1]
       ,[1,0,1,0]]

if adj[1][3] == 1:
    print("b and d are connected")

def print_edges(adj,labels):
    n = len(adj)
    for i in range(n):
        for j in range(i+1,n):
            if adj[i][j] == 1:
                print(labels[i], "--" , labels[j])
                