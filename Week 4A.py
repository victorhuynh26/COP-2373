#This imports time for time related lines to work
import time

#This tracks the amount of time in the program, allowing to see the amount of second there will be after the program ends

def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2-t1)
        return ret_val
    return wrapper


def main():

    #Initializing Variables

    index_dict = []

    spam_hit = 0

    spam_threat= ''

    spam_keywords = ('The IRS is trying to contact you.' + 'You\'ve won.' 'There was an error in transaction.' +
                     'Please verify you bank account.' + 'Free Prize.' + 'Congratulations.' + 'Urgent.' + 'Alert.' +
                     'Refunding.' + 'Cash Prize.' + 'Cheap Deals.' + 'Save Big.' + 'Earn Money.' + '100% Free.' +
                     'Free Trial.' + 'Invest.' + 'Weight Loss.' + 'Cheap.' + 'Risk-Free.' + 'Hurry Now.' + 'Lottery.' +
                     'Winner.' + 'Guarantee.' + 'Limited Time.' + 'Call Now.' + 'Save Big.' + 'Credit Card.' + 'Miracle.' +
                     'Order Now.' + 'Act Now.')

    #This will split all the lines into seperate lines by using a period

    spam_keywords = spam_keywords.split('.')

    #This asks the user if they would like to enter an email

    email_message_asker = input('Would you like to enter a spam phrase/keyword/email? yes or no ')

    #This stops the program for 7 seconds, adding 7 seconds to the timer

    time.sleep(7)

    #If they say yes, then it proceeds. if no, then it stops.

    if email_message_asker.lower() == 'yes':

        #This input asks the user to input their email

        email_message = input('Please input your email ')

        #This puts all the message in lowercase to compare later

        email_message= email_message.lower()

        #This replaces all the periods with spaces and removes all the spaces to make sure that there are no spaces

        email_message = email_message.replace('. ', '.')

        #This for statement checks each line of the spam keywords and checks it with the message. if one is found, then it
        #is added to the list of spam and adds one to the spam hit.

        for sent in spam_keywords:
            if sent.lower() in email_message:
                index_dict.append(sent)
                spam_hit += 1

        #This removes the blank space or '' from the last term from the list and removes one from the counter

        removed = index_dict.pop(-1)
        spam_hit -= 1

        #This if statement will assess the spam level from 0-5, 5-10, and 10+

        if spam_hit >= 0 and spam_hit <= 5:
            spam_threat = 'Low Risk'
        elif spam_hit >= 6 and spam_hit <= 10:
            spam_threat = 'Medium Risk'
        else:
            spam_threat = 'High Risk'

        #This stops the program for 10 seconds and adds 10 seconds to the timer

        time.sleep(10)

        #This prints the spam score, spam threat, and the spam words found.

        print(f'Your Spam Score: {spam_hit}')
        print(f'You are at {spam_threat}')
        print(f'Your Terms: {index_dict}')


#This runs the main function and

main = make_timer(main)
main()