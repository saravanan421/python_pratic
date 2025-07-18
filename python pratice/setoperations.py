# Enter your code here. Read input from STDIN. Print output to STDOUT
def convertion(n,m,arr,like,dislike):
    happiness=0
    for i in arr:
        if i in like:
            happiness+=1
        elif i in dislike:
            happiness-=1
    print(happiness)
        
if __name__=="__main__":
    n,m=[int(x) for x in input().strip().split()]
    arr=input().strip().split(" ")
    like=set(input().strip().split())
    dislike=set(input().strip().split())
    convertion(n,m,arr,like,dislike)
