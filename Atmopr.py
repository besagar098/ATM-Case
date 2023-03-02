from Atmmenu import menu
from Atmexp import DepositeAmntError,WithdrawAmntError,InsuffFundError,LessAmountError
from Atmhit import BalEnq,Deposit,Withdrw
while(True):
    try:
        menu()
        a = int(input("Enter Your Option: "))
        match(a):
            case 1:
                BalEnq()
            case 2:
                try:
                    Deposit()
                except DepositeAmntError:
                    print("Don't enter -ve amount / zero to deposit")
                except ValueError:
                    print("Don't Enter Str,Alnums and Symbols for Deposite Money")
                except LessAmountError:
                    print("Please Deposite more then INR :100.00")
            case 3:
                try:
                    Withdrw()
                except WithdrawAmntError:
                    print("Don't enter -ve amount / zero to Withdraw")
                except InsuffFundError:
                    print("Your Account have Insufficient Balance to Withdraw")
                except ValueError:
                    print("Don't Enter Str,Alnums and Symbols for Withdraw Money")
            case 4:
                print("Thank You For using Sagar's ATM")
                break
            case _:
                print("Your Selection Option is Wrong [PLEASE TRY AGAIN]")
    except ValueError:
        print("Don't Enter Str,Alnums and Symbols for Choice of Operation")



            


