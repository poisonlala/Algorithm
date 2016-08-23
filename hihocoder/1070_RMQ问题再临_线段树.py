n = int(raw_input())
weight = [int(x) for x in raw_input().split()]
ask_times = n = int(raw_input())


class SegmentTreeNode:
    def __init__(self, start, end, m):
        self.start, self.end, self.min = start, end, m
        self.left, self.right = None, None


def query(root, start, end):
    # write your code here
    if not root:
        return 0
    if root.start == start and root.end == end:
        return root.min
    mid = (root.start + root.end) // 2
    result = 0x7FFFFFFF
    if start <= mid:
        result = min(query(root.left, max(start, root.start), min(mid, end)), result)
    if end > mid:
        result = min(query(root.right, max(mid + 1, start), min(end, root.end)), result)
    return result


def build(A):
    # write your code here
    if len(A) == 0:
        return None
    return dfs(A, 0, len(A) - 1)


def dfs(A, lo, hi):
    if lo == hi:
        return SegmentTreeNode(lo, hi, A[lo])
    node = SegmentTreeNode(lo, hi, 0)
    mid = (lo + hi) / 2
    node.left = dfs(A, lo, mid)
    node.right = dfs(A, mid + 1, hi)
    node.min = min(node.left.min, node.right.min)
    return node


def modify(root, index, value):
    # write your code here
    if root.start == root.end and root.end == index:
        root.min = value
    else:
        mid = (root.start + root.end) // 2
        if index > mid:
            modify(root.right, index, value)
        else:
            modify(root.left, index, value)
        root.min = min(root.left.min, root.right.min)


root = build(weight)
for i in range(ask_times):
    (kind, l, r) = (int(x) for x in raw_input().split())
    if kind == 0:
        print query(root,l-1,r-1)
    else:
        modify(root,l-1,r)