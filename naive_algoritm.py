'''To search a pattern in a given text.'''

def search(txt,ptr):
    m=len(ptr)
    n=len(txt)
    # where txt is text and ptr is pattern string
    #along the text
    for i in range(n-m+1):
        j=0
        
        #along the pattern

        for j in range(m):
            if txt[i+j]!=ptr[j]:
                break
            j+=1
        if j==m:
            print("Pattern Found At Index ",i)

txt=input("enetr the string\n")
ptr=input("enter the pattern\n")

search(txt,ptr)
