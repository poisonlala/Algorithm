# get all children
def dfs(parent):
    visited[parent] = True
    all_child[parent].add(parent)
    for child in dic[parent].keys():
        if visited[child]:
            dic[parent].pop(child)
            all_parent[parent] = child
        else:
            all_child[parent] |= dfs(child)
    return all_child[parent]

#insert path
def fixquery(query):
    if query[0] != 1:
        query.insert(0,1)
    for i in range(1,len(query)):
        if query[i] in all_child[query[i-1]]:
            child = query[i]
            while all_parent[child] != query[i-1]:
                query.insert(i,all_parent[child])
                child = all_parent[child]
t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    dic = [{} for x in range(n + 1)]
    all_child = [set() for x in range(n + 1)]
    all_parent =[0]*(n+1)
    visited = [False] * (n + 1)
    for j in range(n - 1):
        (n1, n2) = (int(x) for x in raw_input().split())
        dic[n1][n2] = 1
        dic[n2][n1] = 1
    dfs(1)

    m = int(raw_input())
    query = [int(x) for x in raw_input().split()]
    fixquery(query)
    flag = True
    m=len(query)
    for k in range(m):
        # condition 1:children can't appear infront of parents
        for l in range(k):
            if query[l] in all_child[query[k]]:
                flag = False
                break

        countinued = True
        # condition 2:children must follow the parents
        for l in range(k + 1, m):
            if query[l] not in all_child[query[k]]:
                countinued = False
            if not countinued and query[l] in all_child[query[k]]:
                flag = False
                break

        if not flag:
            break
    if flag:
        print 'YES'
    else:
        print 'NO'
