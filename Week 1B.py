#Student: Victor Huynh

#Assignment: Week 1B

#Description:This program will ask the user if they would like to use the magic eightball. The program will then
#use the magic eightball program and return a statement to the user. This will continue until the user says no.

#This imports random and makes sure that the user will get a random statement from the eightball
import random

#This function creates the file with all the responses with the eightball and then closes the file.
def filecreate():
    file = open('file_response.txt','a')
    sent= ('Yes, of course!\n' + 'Without a doubt, yes.\n' + 'You can count on it.\n' +
           'For sure!\n' + 'Ask me later.\n' + 'I\'m not sure.\n' + 'I can\' tell you right now.'
           + 'No way!\n' + 'I don\'t think so.\n' + 'Without a doubt, no.\n' + 'The answer is clearly NO!')
    file.writelines(sent)
    file.close()

def main():
    #This runs the function above and creates the file
    filecreate()
    #This asks the user if they would like to ask the magic eightball something and takes the yes or no answer
    asker= input('Would you like to answer the magic eightball something? yes or no ')
    #This while loop continuously asks the user if they would like to use the magic eightball and responds if
    #they continue to say yes. This is achived by opening the file and reading the file while using random
    while asker.lower()=='yes':
        eightask=input('Please enter your yes or no question ')
        file=open('file_response.txt').read().splitlines()
        randomline = random.choice(file)
        print(randomline)
        asker = input('Would you like to continue? yes or no ')
    #This force closes the program
    exit()

#This runs the main function
main()