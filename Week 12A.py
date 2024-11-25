# Imports csv and numpy for this program
import csv
import numpy as np


def main():
    # The Initalizing array for the functon which switches the whole csv into numpy array
    array = np.genfromtxt('grades.csv', delimiter=',')

    # This is the empty arrays that will get the scores above a 60% and those who don't

    list_1_pass = np.array([])
    list_1_fail = np.array([])
    list_2_pass = np.array([])
    list_2_fail = np.array([])
    list_3_pass = np.array([])
    list_3_fail = np.array([])

    # This is an empty list which will get the names from the csv file
    list_name = []

    # This opens the csv, which skips the first row (the header), and appends all the names to a list which is assigned to numbers to be used later on
    with open('grades.csv') as opener:
        reader = csv.reader(opener)
        next(reader, None)
        for row in reader:
            list_name.append(row[0])

    # These are the intiazling list that will get the number of students at the end and combine to one list to find the length of the full list
    val_1_list = []
    val_2_list = []
    val_3_list = []
    val_combined_list = []

    # Array Exam 1

    #
    array_exam_1 = array[1:11, 1:2]

    # The below uses np.(blank) which will find the mean, median, std dev, max, and min which will then be printed. The std dev is rounded to the thousands place
    print('Stats for Exam 1\n')

    print(f'The Mean of the grades for exam 1: {np.mean(array_exam_1)}')
    print(f'The Median of the grades for exam 1: {np.median(array_exam_1)}')
    print(f'The Standard Deviation of the grades for exam 1: {round(np.std(array_exam_1), 3)}')
    print(f'The Minimum of the grades for exam 1: {np.min(array_exam_1)}')
    print(f'The Maximum of the grades for exam 1: {np.max(array_exam_1)}\n')

    # This arranges the rows so that it prints out the number of lines in the array for exam 1. It then stacks it on top of array exam 1, so that it becomes a order pair
    # to be used later

    row_num_1 = np.arange(array_exam_1.shape[0])

    pair_1 = np.column_stack((row_num_1, array_exam_1))

    # The below gets each pair from the stacked columns and sees if the value for the pair is equal or above 60%. If yes, then it will be added to the passing list.
    # If not, then it will be added to the failing list. The values specifically added is the number in the list so that it can be called later.

    for pairs in pair_1:
        if pairs[1] >= 60:
            list_1_pass = np.append(list_1_pass, pairs[0])
        else:
            list_1_fail = np.append(list_1_fail, pairs[0])

    # This will convert both of the lists below into integers so that it can be properly printed later

    list_1_pass = list_1_pass.astype(int)
    list_1_fail = list_1_fail.astype(int)

    # This uses the pass_list and for each value it will use the number from the pass_list and call it in the name list. This will effectively get the name from the list.
    # it will make it equal to val which will be added to another list for later and then it will print it.

    print('Students who Passed:')
    for value_1_pass in list_1_pass:
        val_1 = (list_name[value_1_pass])
        val_1_list.append(val_1)
        print(val_1)

    # This gets each value from the fail_list and calls it from the name list. It will then print each called name.

    print('\nStudents who Failed:')
    for value_1_fail in list_1_fail:
        print(list_name[value_1_fail])

    # Array Exam 2

    # The below is exactly the same for array exam 1, except it changes the values to exam two by the array changing what values if focuses on. It also uses any
    # initialzing values above, except it uses the number 2

    array_exam_2 = array[1:11, 2:3]

    print('\nStats for Exam 2\n')

    print(f'The Mean of the grades for exam 1: {np.mean(array_exam_2)}')
    print(f'The Median of the grades for exam 1: {np.median(array_exam_2)}')
    print(f'The Standard Deviation of the grades for exam 1: {round(np.std(array_exam_2), 3)}')
    print(f'The Minimum of the grades for exam 1: {np.min(array_exam_2)}')
    print(f'The Maximum of the grades for exam 1: {np.max(array_exam_2)}\n')

    row_num_2 = np.arange(array_exam_2.shape[0])

    pair_2 = np.column_stack((row_num_2, array_exam_2))

    for pairs in pair_2:
        if pairs[1] >= 60:
            list_2_pass = np.append(list_2_pass, pairs[0])
        else:
            list_2_fail = np.append(list_2_fail, pairs[0])

    list_2_pass = list_2_pass.astype(int)
    list_2_fail = list_2_fail.astype(int)

    print('Students who Passed:')
    for value_2_pass in list_2_pass:
        val_2 = (list_name[value_2_pass])
        val_2_list.append(val_2)
        print(val_2)
    print('\nStudents who Failed:')
    for value_2_fail in list_2_fail:
        print(list_name[value_2_fail])

    # Array Exam 3

    # The below is exactly the same for array exam 1, except it changes the values to exam three by the array changing what values if focuses on. It also uses any
    # initialzing values above, except it uses the number 3

    array_exam_3 = array[1:11, 3:4]

    print('\nStats for Exam 3\n')

    print(f'The Mean of the grades for exam 1: {np.mean(array_exam_3)}')
    print(f'The Median of the grades for exam 1: {np.median(array_exam_3)}')
    print(f'The Standard Deviation of the grades for exam 1: {round(np.std(array_exam_3), 3)}')
    print(f'The Minimum of the grades for exam 1: {np.min(array_exam_3)}')
    print(f'The Maximum of the grades for exam 1: {np.max(array_exam_3)}\n')

    row_num_3 = np.arange(array_exam_3.shape[0])

    pair_3 = np.column_stack((row_num_3, array_exam_3))

    for pairs in pair_3:
        if pairs[1] >= 60:
            list_3_pass = np.append(list_3_pass, pairs[0])
        else:
            list_3_fail = np.append(list_3_fail, pairs[0])

    list_3_pass = list_3_pass.astype(int)
    list_3_fail = list_3_fail.astype(int)

    print('Students who Passed:')
    for value_3_pass in list_3_pass:
        val_3 = (list_name[value_3_pass])
        val_3_list.append(val_3)
        print(val_3)
    print('\nStudents who Failed:')
    for value_3_fail in list_3_fail:
        print(list_name[value_3_fail])

    # Array Total Stats

    # This calls all the numbers from the array and excludes any headers

    array_total = array[1:11, 1:4]

    # Like above this finds the stats for all the exams combined

    print('\nStats for all Exams\n')

    print(f'The Mean of the grades across all exams: {np.mean(array_total)}')
    print(f'The Median of the grades across all exams: {np.median(array_total)}')
    print(f'The Standard Deviation of the grades across all exams: {round(np.std(array_total), 3)}')
    print(f'The Minimum of the grades across all exams: {np.min(array_total)}')
    print(f'The Maximum of the grades across all exams: {np.max(array_total)}')

    # This will combine all the lists above from the passed lists together. It will then find the length of the list so that we can know how many passed test scores there are.

    val_combined_list = val_1_list + val_2_list + val_3_list
    pass_rate = len(val_combined_list)

    # This then gets the pass_rate length and divides it by 30, the number of total exams. It will then by multiplied by 100 and rounded to the hundreths places to
    # find the pass rate.

    print(f'\nThe Pass Rate of all exams: {round((pass_rate / 30) * 100, 2)}%')


main()