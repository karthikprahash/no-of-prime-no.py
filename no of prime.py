# no-of-prime-no.py
i,j=map(int,input().split())
if i<=j<=1000:
    count=0
    for num in range(i,j+1):
        if num >1:
            for t in range(2,num):
                if (num%t)==0:
                    break
            else:
                count=count+1
    print(count)
                    
        
       
                        
