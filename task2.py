def listofsum(arr):
    ans=0
    for i in arr:
        ans+=i
    print("Sum ",ans)
def listofmaxvalue(arr):
    ans=arr[0]
    for i in arr:
        if ans<i:
            ans=i
    print("Max ",ans)
def main():
    arr=[]
    n=int(input("Enter number of elements in list"))
    for i in range(0,n):
        arr.append(int(input(f"Enter element {i} ")))
    listofsum(arr)
    listofmaxvalue(arr)
if __name__=="__main__":
    main()