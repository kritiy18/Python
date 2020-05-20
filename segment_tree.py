'''Implementation of segment tree for min query'''

import math

#build tree
def buildtree(tree,l,index,s,e):
	if s>e:
		return

	if s==e:
		tree[index]=l[s]
		return

	mid=(s+e)//2

	#build left and right subtree
	buildtree(tree,l,2*index,s,mid)
	buildtree(tree,l,2*index+1,mid+1,e)

	left=tree[2*index]
	right=tree[2*index+1]

	tree[index]=min(left,right)


#to get min query
def query(tree,index,s,e,qs,qe):
	if qs>e or qe<s:
		return math.inf

	if s>=qs and e<=qe:
		return tree[index]

	mid=(s+e)//2

	leftans=query(tree,2*index,s,mid,qs,qe)
	rightans=query(tree,2*index+1,mid+1,e,qs,qe)

	return min(leftans,rightans)


#update a node
def updateNode(tree,index,s,e,i,value):
	if i<s or i>e:
		return

	if s==e:
		tree[index]=value
		return

	mid=(s+e)//2

	updateNode(tree,2*index,s,mid,i,value)
	updateNode(tree,2*index+1,mid+1,e,i,value)

	tree[index]=min(tree[2*index],tree[2*index+1])
	return


#update a range
def updateRange(tree,index,s,e,rs,re,value):
	if re<s or rs>e:
		return

	if s==e:
		tree[index]+=value
		return

	mid=(s+e)//2

	updateRange(tree,2*index,s,mid,rs,re,value)
	updateRange(tree,2*index+1,mid+1,e,rs,re,value)

	tree[index]=min(tree[2*index],tree[2*index+1])
	return



print("enter the array :")
l=list(map(int,input().split()))
n=len(l)
tree=[None]*(4*n+1)
index=1
s=0
e=n-1
buildtree(tree,l,index,s,e)


print("enter number of query :")
for _ in range(int(input())):
	print("enter the query range")
	qs,qe=list(map(int,input().split()))
	print(query(tree,index,s,e,qs,qe))