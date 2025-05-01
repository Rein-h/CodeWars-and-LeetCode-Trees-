"""Delete Node in a BST"""

def tree_by_levels(node):
    if not node:
        return []

    result = [node.value]
    queue = [node]
    
    while True:
        q = []
        for node in queue:
            if node.left:
                result.append(node.left.value)
                q.append(node.left)
            if node.right:
                result.append(node.right.value)
                q.append(node.right)

        queue = q
        if not queue:
            break
    
    return result
