def main():
    index_dict = []

    spam_hit = 0

    spam_threat= ''

    spam_keywords = ('The IRS is trying to contact you.' + 'You\'ve won.' 'There was an error in transaction.' +
                     'Please verify you bank account.' + 'Free Prize.' + 'Congratulations.' + 'Urgent.' + 'Alert.' +
                     'Refunding.' + 'Cash Prize.' + 'Cheap Deals.' + 'Save Big.' + 'Earn Money.' + '100% Free.' +
                     'Free Trial.' + 'Invest.' + 'Weight Loss.' + 'Cheap.' + 'Risk-Free.' + 'Hurry Now.' + 'Lottery.' +
                     'Winner.' + 'Guarantee.' + 'Limited Time.' + 'Call Now.' + 'Save Big.' + 'Credit Card.' + 'Miracle.' +
                     'Order Now.' + 'Act Now.')

    spam_keywords = spam_keywords.split('.')

    email_message_asker = input('Would you like to enter a spam phrase/keyword/email? yes or no ')

    if email_message_asker.lower() == 'yes':

        email_message = input('Please input your email ')

        email_message= email_message.lower()

        email_message = email_message.replace('. ', '.')

        for sent in spam_keywords:
            if sent.lower() in email_message:
                index_dict.append(sent)
                spam_hit += 1

        removed = index_dict.pop(-1)
        spam_hit -= 1

        if spam_hit >= 0 and spam_hit <= 5:
            spam_threat = 'Low Risk'
        elif spam_hit >= 6 and spam_hit <= 10:
            spam_threat = 'Medium Risk'
        else:
            spam_threat = 'High Risk'

        print(f'Your Spam Score: {spam_hit}')
        print(f'You are at {spam_threat}')
        print(f'Your Terms: {index_dict}')


main()
