class Node:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.data=val

#function to do inorder traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=" ")
		inorder(root.right)

#function to do preorder traversal
def preorder(root):
	if root:
		print(root.data,end=" ")
		preorder(root.left)
		preorder(root.right)

#function to do postorder traversal
def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.data,end=" ")

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

print("inorder traversal : ")
print(inorder(root))
print("preorder traversal : ")
print(preorder(root))
print("postorder traversal : ")
print(postorder(root))
