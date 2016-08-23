# def dfs(parent):
#     node[parent] = 1
#     for child in tree[parent].keys():
#         if level[child] == 0:
#             level[child] = level[parent] + 1
#             dfs(child)
#             node[parent] += node[child]
#             total[0] += tree[parent][child] * node[child] * (n - node[child])

def dfs():
    queue =[1]
    q = [1]
    while len(queue):
        parent = queue[0]
        del queue[0]

        for child in tree[parent].keys():
            if level[child] ==0:
                queue.append(child)
                q.append(child)
                parent_node[child] = parent
                level[child] = level[parent]+1

    for i in range(len(q)-1,0,-1):
        child = q[i]
        node[parent_node[child]] += node[child]
        total[0] += tree[parent_node[child]][child]*node[child]*(n-node[child])


(n, m) = (int(x) for x in raw_input().split())
level = [0] * (n + 1)
node = [1] * (n + 1)
total = [0]
level[1] = 1
tree = [{} for x in range(n+1)]
parent_node = {}

for i in range(n - 1):
    (parent, child, weight) = (int(x) for x in raw_input().split())
    tree[parent][child] = weight
    tree[child][parent] = weight

dfs()

for i in range(m):
    s = raw_input()
    if s == 'QUERY':
        print total[0]
    else:
        (p, c, w) = (int(x) for x in s[5:].split())
        if level[p] > level[c]:
            tmp = p
            p = c
            c = tmp
        add = w - tree[p][c]
        total[0] += add * node[c] * (n - node[c])
        tree[p][c] = w
        tree[c][p] = w