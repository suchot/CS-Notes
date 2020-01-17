class TreeNode():
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
class Solution():

    def serialbyPre(self, root):
        res = ""
        if not root:
            return '#!'
        res =  str(root.val) +'!'
        res += self.serialbyPre(root.left)
        res += self.serialbyPre(root.right)
        return res
    def serialByLevel(self, root):
        res = ''
        if not root:
            return '#!'
        res = str(root.val) + '!'
        queue  =  [root]
        while queue != []:
            node = queue.pop(0)
            if node.left:
                res += str(node.left.val)+ '!'
                queue.append(node.left)
            else:
                res += '#!'
            if node.right:
                res += str(node.right.val) + '!'
                queue.append(node.right)
            else:
                res += '#!'
        return res
if __name__ == "__main__":
    n,root = map(int, input().split())
    dict_Node = {root:TreeNode()}
    for i in range(n):
        fa, lch, rch= map(int, input().split())
        if dict_Node.get(fa) is None:
            dict_Node[fa]=TreeNode()
        if lch != 0 and dict_Node.get(lch) is None:
            dict_Node[lch]= TreeNode()
            dict_Node[fa].left = dict_Node[lch]
        if rch != 0 and dict_Node.get(rch) is None:
            dict_Node[rch]= TreeNode()
            dict_Node[fa].right = dict_Node[rch]
        dict_Node[fa].val = fa


    # for i in range(n):
    #     fa, lch, rch = map(int, input().split())
    #     dict_node.get(fa, TreeNode())
    #     if lch != 0 and dict_node.get(lch, TreeNode()):
    #         dict_node[fa].left = dict_node[lch]
    #     if rch != 0 and dict_node.get(lch, TreeNode()):
    #         dict_node[fa].right = dict_node[rch]
    #     dict_node[fa].val = fa
    S = Solution()
    print(S.serialbyPre(dict_Node[root]))
    print(S.serialByLevel(dict_Node[root]))
   
   