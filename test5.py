print("="*50) 
print("       BANK ACCOUNT MANAGEMENT SYSTEM")
print("="*50)

while True:
   print("A. CREATE NEW ACCOUNT" )
   print("B. CHECK ACCOUNT DETAIL")
   print("C. WITHDRAW MONEY ")
   print("D. DEPOSIT MONEY")
   print("E. CHECK ACCOUNT BALANCE ")
   print("F. DISPLAY ALL ACCOUNT ")
   print("G. EXIT ")

   a = input("enter a value: ").upper()
   match a: 
      
            case "A":
              print("create a new account ")  

            case "B":
             print("check account detail ")

            case "C":
             print("withdraw money ")

            case "D":
             print("deposit money")

            case "E":
             print("check account balance ")
            case "F":
             print("display all account" ) 
            case "G": 
             print("exit")
             
            case _:
             print("invalid")  
             break
             