def search(txt,ptr):
    m=len(ptr)
    n=len(txt)
    # where txt is text and ptr is pattern string
    for i in range(n-m+1):
        j=0
        for j in range(m):
            if txt[i+j]!=ptr[j]:
                break
            j+=1
        if j==m:
            print("Pattern Found At Index ",i)

txt=input("enetr the string\n")
ptr=input("enter the pattern\n")

search(txt,ptr)
