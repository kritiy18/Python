'''function for the lazy propagation'''

def updatelazy(tree,lazy,index,s,e,rs,re,value):
	if s>e:
		return

	if lazy[index]!=0:
		tree[index]+=lazy[index]
		if s!=e:
			lazy[2*index]+=lazy[index]
			lazy[2*index+1]+=lazy[index]
		lazy[index]=0

	#no overlap
	if rs>e or re<s:
		return

	#total overlap
	if rs<=s and re>=e:
		tree[index]+=value
		if s!=e:
			lazy[2*index]+=value
			lazy[2*index+1]+=value
		return

	#partial overlap
	mid=(s+e)//2
	updatelazy(tree,lazy,2*index,s,mid,rs,re,value)
	updatelazy(tree,lazy,2*index+1,mid+1,e,rs,re,value)
	tree[index]=min(tree[2*index],tree[2*index+1])


if __name__ == '__main__':
	main()