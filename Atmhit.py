from Atmexp import DepositeAmntError,WithdrawAmntError,InsuffFundError,LessAmountError
Bal = 500.00
def BalEnq():
    print("Your Current Balance is INR: {}".format(Bal))
def Deposit():
    global Bal
    depamt=float(input("Enter the Amount you want to Deposite: "))
    if(depamt<=0):
         raise DepositeAmntError
    elif(depamt<100):
        raise LessAmountError
    else:
        Bal= Bal + depamt
        print("Your Account xxxxxx123 creadited with INR:{}".format(depamt))
        print("Your Current Balance is INR:{}".format(Bal))

def Withdrw():
    global Bal
    wdrwamt= float(input("Enter the Amount you want to Withdraw: "))
    if(wdrwamt<=0):
        raise WithdrawAmntError
    elif((wdrwamt+500)>Bal):
        raise InsuffFundError
    else:
        Bal = Bal - wdrwamt
        print("Your Account xxxxxx123 debited with INR:{}".format(wdrwamt))
        print("Your Current Balance is INR:{}".format(Bal))

    



   




