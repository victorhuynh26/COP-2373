#This imports CSV

import csv

def main():

    #These are the initalizing dictionary and list that will hold those dictionaries

    mydict = []

    dict_adder = {}

    #These two ask the user if they would like to input students grades and will continue if they say yes

    initial_asker = input('Would you like to input student grades? yes or no ')

    if initial_asker.lower() == 'yes':

        #These two first asks the user how many students they would like to enter and makes a for loop for that many students

        number_asker = int(input('How many students would you like to enter? '))

        for length in range(number_asker):

            #These few lines asks the user the name of the student and the grades they achieved on the exams

            name_asker= input('Enter the name of the student ')
            grade_asker_1 = int(input('Enter the student grade for exam 1 '))
            grade_asker_2 = int(input('Enter the student grade for exam 2 '))
            grade_asker_3 = int(input('Enter the student grade for exam 3 '))

            #This line appends the dictionary to the list, with the most recent student being added as the loop goes on

            mydict.append({'Name' : name_asker, 'Exam 1': grade_asker_1, 'Exam 2': grade_asker_2,'Exam 3': grade_asker_3})

    #This is the headers that will line up with the various information later on

    headers = ['Name', 'Exam 1', 'Exam 2', 'Exam 3']

    #This CSV program will write in rows to the grades.csv and add the header to the top

    with open('grades.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= headers)

        writer.writeheader()

        writer.writerows(mydict)

    #This CSV program will read and print the row in the grades.csv by using a for loop

    with open('grades.csv', 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            print(row)

#This runs the main function
main()


