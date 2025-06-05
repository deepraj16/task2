def lower_traingle(n): 
     for i in range(n): 
        for j in range(i,n): 
            print(" ",end="")
        for k in range(i): 
            print("*",end="")
        for k in range(i-1): 
            print("*",end="")    
        print()  

def upper_traingle(n): 
     for i in range(n,0,-1): 
        for j in range(i,n): 
            print(" ",end="")
        for k in range(i): 
            print("*",end="")
        for k in range(i-1): 
            print("*",end="")    
        print()


def draw_pyramid(n):    
      lower_traingle(n)
      upper_traingle(n)
    

try :
    n=int(input("Enter the height of pyramid : "))
    if n > 30:
        raise ValueError("Pyramid height too large. Please enter a value ≤ 30.")
    if n < 1:
        raise ValueError("Pyramid height must be a positive integer.")
    print("Upper triangular : ") 
    lower_traingle(n)
    print()
    print("Lower triangular : ")
    print()
    upper_traingle(n)
    print()
    print("The pyramid: ")
    draw_pyramid(n)

except ValueError as e:
    print("Error:", e)    
except : 
    print("Plese enter only  integer") 