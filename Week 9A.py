class BankAcct:

    #This sets up the init for the class and for all the bank info

    def __init__(self):
        self.name = []
        self.accountnumber = []
        self.amount = []
        self.intrest = []

    #This sets up append which will allow the list to be changed

    def append(self, change):
        self.name.append(change)
        self.accountnumber.append(change)
        self.amount.append(change)
        self.intrest.append(change)

    #This sets up the clear, which will allow the current list to be cleared

    def clear(self):
        self.name.clear()
        self.accountnumber.clear()
        self.amount.clear()
        self.intrest.clear()

    #This sets up pop, which deletes the list while returning it

    def pop(self):
        return self.name.pop()
        return self.accountnumber.pop()
        return self.amount.pop()
        return self.intrest.pop()

def main():

    #This will run the class and put into the integer bank

    bank = BankAcct()

    #These two lines ask the user if they would like to make a bank account, if yes then it will continue

    initital_asker = input('Would you like to make a bank account? yes or no ')

    if initital_asker.lower() == 'yes':

        #These next lines will ask the user to input the various bank information and will append it to the class. It will then print the various terms in the class

        name = input('Please input your name ')
        accountnumber = input('Please input an account number ')
        amount = int(input('Please input how much you would like to deposit '))
        intrest = input('Please input your intrest rate ')

        bank.name.append(name)
        bank.accountnumber.append(accountnumber)
        bank.amount.append(amount)
        bank.intrest.append(intrest)

        print(bank.name)
        print(bank.accountnumber)
        print(bank.amount)
        print(bank.intrest)

        #These two lines will ask the user if they would like to change their bank information, and puts it in a while loop to allow the user to keep using it until they say no

        change_asker = input('Would you like to change your information? yes or no ')

        while change_asker.lower() == 'yes':

        #This line will ask the user what specific part of their bank information they would like to change and uses if statements for each scenario

            change_specific = input('What would you like to change: name, account number, amount, intrest rate ')

            #This will ask the user to input their changed information, and then it will clear the previous information to append the new information.
            #It will then print the new information in their account.

            if change_specific.lower() == 'name':

                changer = input('Please input the changed name ')

                bank.name.clear()

                bank.name.append(changer)

                print('Here is the changed Information')

                print(bank.name)
                print(bank.amount)
                print(bank.accountnumber)
                print(bank.intrest)

                change_asker = input('Would you like to continue to change your information? yes or no ')

            # This will ask the user to input their changed information, and then it will clear the previous information to append the new information.
            # It will then print the new information in their account.

            elif change_specific.lower() == 'account number':

                changer = input('Please input the changed account number ')

                bank.accountnumber.clear()

                bank.accountnumber.append(changer)

                print('Here is the changed Information')

                print(bank.name)
                print(bank.amount)
                print(bank.accountnumber)
                print(bank.intrest)

                change_asker = input('Would you like to continue to change your information? yes or no ')

            #This is different because it comes in two parts. It first asks the user if they would like to withdraw or deposit and then uses if statements for what the
            #user inputted. If they deposit it will ask the user to input how much they would like to deposit and then pops the term in the list to add the amount.
            #It will then append it and print their bank info. If they withdraw it will ask the user to input how much they would like to deposit and then pops the term
            #in the list to subtract the amount. It will then append it and print their bank info.

            elif change_specific.lower() == 'amount':

                deposit_withdraw = input('Would you like to deposit or withdraw ')

                if deposit_withdraw.lower() == 'deposit':

                    changer = int(input('Please input the amount you want to deposit '))

                    amount = bank.amount.pop()

                    amount = amount + changer

                    bank.amount.clear()

                    bank.amount.append(amount)

                    print('Here is the changed Information')

                    print(bank.name)
                    print(bank.amount)
                    print(bank.accountnumber)
                    print(bank.intrest)

                    change_asker = input('Would you like to continue to change your information? yes or no ')

                else:

                    changer = int(input('Please input the amount you want to withdraw '))

                    amount = bank.amount.pop()

                    amount = amount - changer

                    bank.amount.clear()

                    bank.amount.append(amount)

                    print('Here is the changed Information')
                    print(bank.name)
                    print(bank.amount)
                    print(bank.accountnumber)
                    print(bank.intrest)

                    change_asker = input('Would you like to continue to change your information? yes or no ')

            #This else statement is saved for intrest rate and like the rest will clear and append the list from the class. It will then print

            else:

                changer = input('Please input the new intrest rate ')

                bank.intrest.clear()

                bank.intrest.append(changer)

                print('Here is the changed Information')

                print(bank.name)
                print(bank.amount)
                print(bank.accountnumber)
                print(bank.intrest)

                change_asker = input('Would you like to continue to change your information? yes or no ')



#This runs the main function
main()