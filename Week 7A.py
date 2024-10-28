import re

def main():

    #This counter is used to track the amount of sentences there are in the paragraph/sentences.

    count= 0

    #This the pattern used in the re.findall and allows capital and number letters for the sentence to begin.

    pattern = r'[A-Za-z0-9].*?[.!?](?! [a-z]|\w)'

    #This asks the user if they would like to enter in the program

    initial_asker=input('Would you like for this program to tell how many sentences in a paragraph? Yes or No ')

    if initial_asker.lower() == 'yes':

        #This is the input which asks the user to input their paragraph. Note: the letters must start with capital letters

        paragraph_asker = input('Please enter your paragraph. (Make sure that starting letters in the sentence are capitalized) ')

        #this re.findall searches for the separate sentences with the pattern and the paragraph asker

        math = re.findall(pattern, paragraph_asker, flags=re.DOTALL)

        #This for each line in the re.findall prints the sentence to show and adds to the total amount of sentences

        for line in math:
            print('-', line)
            count +=1

        #This prints the total amount of sentences

        print(f'The amount of sentences are {count}')

#This runs the program
main()