def binary(num):
    if num>=1:
        binary(num//2)
        print(num%2, end=' ')
inp=int(input("Enter number : "))
if __name__=="__main__":
    binary(inp)