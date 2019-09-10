m,n = map(int,input().split(" "))
mem = {"*":None}
degree = set()
class ListNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
for _ in range(m):
    root,left,right = input().split()
     
    if root not in mem:
        mem[root] = ListNode(root)
    if left not in mem:
        mem[left] = ListNode(left)
    if right not in mem:
        mem[right] = ListNode(right)
    #建图，这种用dict复制图的方法的常见方法
    degree.add(left)
    degree.add(right)
     
    _root,_left,_right = mem[root],mem[left],mem[right]
    _root.left = _left
    _root.right = _right
 
#root 节点是入度为0的节点  
root = (set(mem) - degree).pop()
 
global ans
ans = []
#DFS，常规操作
def dfs(root):
    global ans
    if root:
        left = dfs(root.left)
        right = dfs(root.right)
        this = left + right + 1
        if this >= n + 1:
            ans.append(root.val)
        return this
    return 0
dfs(mem[root])
if ans:
    print(" ".join(ans))
else:
#None也要print出来，不然会少一个回车符
    print(None)