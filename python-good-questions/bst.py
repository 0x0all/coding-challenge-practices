# 1. Initialize, low = MAX_VALUE, high = MIN_VALUE.
# 2. If root.data <= low || root.data >= high, return false.
# 3. Recursively check for left sub tree and right sub tree.
#    a. For left sub tree, pass high as root.data because for a BST, root forms an upper bound for left sub tree node values.
#    b. For right sub tree, pass low as root.data because for a BST, root forms a lower bound for right sub tree node values.
# Time complexity: O(n)

def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))
 
# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))
 