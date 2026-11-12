

input("enter a number:")

def main(x:int):
    # Remove pass with your answer.
    x = int(input("enter a number:"))    
if x % 10 == 0 and  x % 3 != 0:
    print(f'{x} is divisible by 10 and not divisible by 3 ')
else :
    print(f'{x} is not divisible by 10 and not divisible by 3')

      



if __name__ == "__main__":
    # execute only if run as a script
    main()
