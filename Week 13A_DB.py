#These imports the necessary modules needed for this program to work
import sqlite3
import csv
import matplotlib.pyplot as plt


def database(data):

    #This connects the sqlite3 with a database called population
    connection = sqlite3.connect('population_VH.db')

    #this makes a cursor which connects with the database
    cursor = connection.cursor()

    #this deletes any previous entries in the database (This is caused by repeats in the code)
    cursor.execute('DELETE FROM population')

    #This commits the changes from the deletes
    connection.commit()

    #This creates the table and makes three headers: city, year, and population
    cursor.execute('''CREATE TABLE IF NOT EXISTS population
                (city Text, year INTEGER, population INTEGER)''')

    #This executes multiple which inserts the population, year, and city from the data that it is fed
    cursor.executemany('INSERT INTO population(city, year, population) VALUES(?,?,?)',
                       data)

    #These commits the changes and closes the database
    connection.commit()
    connection.close


def year_skipped():

    #These are all the names of the cities from florida
    city_name = ['Palm Beach', 'Clearwater', 'Lehigh Acres', 'Spring Hills',
                 'Brandon', 'Lakeland', 'Fort Lauderdale', 'Tallahassee',
                 'St. Petersburg', 'Tampa']

    #This is the initial population number and will be used later to calulcate the population
    population_number = [118709, 116616, 123751, 114706, 115330, 110401, 182247,
                         195057, 258245, 380476]

    #This is the initial population which will be used to find all the years from 20 years from now
    year_list = [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023]

    #This contains the initial population and will contain all the populations in the future
    population_data = [118709, 116616, 123751, 114706, 115330, 110401, 182247,
                         195057, 258245, 380476]

    #This contains all the years from 2023 and the years 20 years from now to 2043
    full_year = [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023]


    #This loop will happen from 20 years and find the population growth from the equation and round it. It will then be added to population data
    for year in range(1, 21):
        new_population_size = [(i*((1.02)**year)) for i in population_number]
        new_population_size = [round(d) for d in new_population_size]
        population_data.extend(new_population_size)

    #This loop will add the 10 of each year from 2023-2043 by adding one to each for 20 times and add it to a list
    for years in range(1,21):
        new_year_list = [(s + years) for s in year_list]
        full_year.extend(new_year_list)

    #This will multiply the list so that there will be 21 pairs for the 20 years in the future
    city_name = city_name * 21

    #This will contain all the years from 2023-2043 and will be grouped by their year 2023 togther for example
    year_split= []

    #This will contain all the city names together in groups of 20
    city_split = []

    #This will contain all the population data that is split into each sepearte city for 20 years
    split_city = []


    #These ranges below will basically get every 10th item and put them together in groups of 10. It will then move to the 2nd term
    #and get every 10th item and slowly work up until the 10th item which will get every group and number together

    for pop in range(0, 10):
        for q in range(pop, len(population_data), 10):
            split_city.append(population_data[q])

    for yr in range(0, 10):
        for p in range(yr, len(full_year), 10):
            year_split.append(full_year[p])

    for cit in range(0, 10):
        for l in range(cit, len(city_name), 10):
            city_split.append(city_name[l])

    #This will pair up all the city, year, and population together into groups of three in a list
    all_data = [(city_split[i], year_split[i], split_city[i]) for i in range(0, len(city_split))]

    #This will call the database function and will put the data caluclated and run it through the database
    database(all_data)



def main():

    #This will ask if they would like to see the population growth. If yes, then it will continue. If no, then it will end.
    initial_asker = input('Would you like to see graphs for predicted population\n'
                          'growth for cities in Florida? yes or no. ')

    #This while will make sure that they can keep continuing
    while initial_asker.lower() == 'yes':

        #This connects the database will sql3 and the database
        connection = sqlite3.connect('population_VH.db')

        #This makes the cursor
        cursor = connection.cursor()

        #This runs the calculations for the 20 years and puts them into the database
        year_skipped()

        #This will get all the information from the population database
        cursor.execute('SELECT * FROM population')

        #This will write all the data from the database and put it into a csv file while fetching all the information from the database
        with open('population.csv', 'w', newline='') as csv_file:

            writer_pop = csv.writer(csv_file)

            writer_pop.writerows(cursor.fetchall())

        #This will ask the user which city they would like to view
        city_asker = input('Which City would you like to see? Palm Beach, Clearwater, Lehigh Acres,\n'
                           'Spring Hills, Brandon, Lakeland, Fort Lauderdale, Tallahassee,\n'
                           'St. Petersburg, Tampa (Note: Please keep spelling Exact) ')

        #This will use the answer above so that they can get the specific city so that they can view the city
        cursor.execute(f'SELECT year, population FROM population WHERE city = "{city_asker}" ORDER BY year')

        #This will fetch all the specific data
        data = cursor.fetchall()

        #This will get all specific data by getting the population and years from the specified city
        years = [row[0] for row in data]
        population_count = [row[1] for row in data]

        #This will plot all the information from the information and will plot the graph
        plt.figure(figsize=(10, 6))
        plt.plot(years, population_count, marker='o', color='r', linestyle='-', label=f'{city_asker} Population')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title(f'{city_asker} population over 20 years')
        plt.show()

        #this will ask the user if they would like to continue. If yes, then the program will continue.
        initial_asker = input('Would you like to go again? yes or no ')

#This runs the main function
main()