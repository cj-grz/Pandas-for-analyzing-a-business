# Author name: Carlos Justin Briones Valdez, Midori Michel González, Luis Felipe R. González   
# Student ID: A01634640, A01639727, A01252326
# Date: October/2020
# Algorithm: Final proyect: Data  analyzer for business.

# Importing the necessary libraries 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setting a password
print('Set your password in numbers')
r = input()

# Defining a function for our menu
def get_menu_choice():
    def print_menu():       
        print(30 * "-", "COMPANY MENU", 30 * "-")
        print("1. See information about the most sold items from the month ")
        print("2. See information about the customers who made bigger transactions last month ")
        print("3. see information about the least sold items ")
        print("4. See sales throught time ")
        print("5. Exit ")
        print(73 * "-")
# Setting the loop for functioning
    loop = True
    int_choice = -1

# While loopp and conditionals that determine which action is performed depending on the user's input
    while loop:
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")  # User's input
        if choice == '1':
            int_choice = 1
            loop = False
             # start defining variables
            print('Enter the path to the excel file')
            df = pd.read_excel(input()) # put the path for the excel file to read
            list1 = df['Precio total']
            sr = list1.nlargest(5)
            print('The maximun total price of a product was:', list1.max()) # 5 indicators
            print('The average price of the 5 most sold pproducts is:', sr[:5].mean())
            print('The average price for all products is:', list1.mean())
            print('The lowest value of the 5 most sold pproducts is:', sr[:5].min())
            print('To see the 5 most sold products see the graph:')
            sr = np.array(sr)
            name0 = df[df['Precio total']==sr[0]]['Nombre producto'].values # Retrieves a value matching it with a known value
            name1 = df[df['Precio total']==sr[1]]['Nombre producto'].values
            name2 = df[df['Precio total']==sr[2]]['Nombre producto'].values
            name3 = df[df['Precio total']==sr[3]]['Nombre producto'].values
            name4 = df[df['Precio total']==sr[4]]['Nombre producto'].values
            # Start setting the graphs
            plt.bar([str(name0), str(name1) , str(name2) , str(name3) , str(name4)], [sr[0], sr[1], sr[2], sr[3], sr[4]], color=['green'])
            plt.xlabel ("Name of the product")
            plt.ylabel ("price of the product")
            plt.title ("5 most sold pproducts this month") 
            plt.show()
            ip0 = df[df['Precio total']==sr[0]]['Precio unidad'].values # Retrieves a value matching it with a known value
            ip1 = df[df['Precio total']==sr[1]]['Precio unidad'].values
            ip2 = df[df['Precio total']==sr[2]]['Precio unidad'].values
            ip3 = df[df['Precio total']==sr[3]]['Precio unidad'].values
            ip4 = df[df['Precio total']==sr[4]]['Precio unidad'].values
            plt.bar([str(name0), str(name1) , str(name2) , str(name3) , str(name4)], [int(ip0), int(ip1), int(ip2), int(ip3), int(ip4)], color=['green'])
            plt.xlabel ("Name of the product")
            plt.ylabel ("individual price of the product")
            plt.title ("individual price of the 5 most sold pproducts this month")
            plt.show()
        elif choice == '2': # Second option
            int_choice = 2
            loop = False
             # start defining variables
            print('Enter the path to the excel file')
            df = pd.read_excel(input()) # put the path for the excel file to read
            list1 = df['Precio total']
            sr = list1.nlargest(5)
            nameOfCustomer = df['Nombre']
            cus = df.groupby('Nombre').size()
            cus = np.array(cus)
            sr = np.array(sr)
            print('The customer that made more transactions was', nameOfCustomer[cus[0]])   # 5 indicators
            print('The average transaction was of:',list1.mean())
            print('The customer who bought the least was:', nameOfCustomer[cus[-1]])
            minC= df[df['Precio total']==list1.min()]['Nombre'].values
            print('The lowest value of a transaction was made by:', minC[-1])
            print('To see the 5 most frequent clients see the graph:')
            name0 = df[df['Nombre']==nameOfCustomer[cus[0]]]['Nombre producto'].values # Retrieves a value matching it with a known value
            name1 = df[df['Nombre']==nameOfCustomer[cus[1]]]['Nombre producto'].values
            name2 = df[df['Nombre']==nameOfCustomer[cus[2]]]['Nombre producto'].values
            name3 = df[df['Nombre']==nameOfCustomer[cus[3]]]['Nombre producto'].values
            name4 = df[df['Nombre']==nameOfCustomer[cus[4]]]['Nombre producto'].values
             # Start setting the graphs
            plt.scatter([str(nameOfCustomer[cus[0]]), str(nameOfCustomer[cus[1]]) , str(nameOfCustomer[cus[2]]) , str(nameOfCustomer[cus[3]]) , str(nameOfCustomer[cus[4]])], [str(name0[0]), str(name1[0]), str(name2[0]), str(name3[0]), str(name4[0])], color=['red'])
            plt.xlabel ("Name of the product")
            plt.ylabel ("Client")
            plt.title ("Items bought by the most frequent client")
            plt.show()
        elif choice == '3':
            int_choice = 3
            loop = False
             # start defining variables
            print('Enter the path to the excel file')
            df = pd.read_excel(input()) # put the path for the excel file to read
            list1 = df['Precio total']
            sr = list1.nlargest(5)
            mask = list1 != 0
            list2 = df[mask].sort_values('Precio total', ascending=True) # sorts values
            list2 = list2['Precio total']
            list2 = np.array(list2)
            print('From the least sold products, the maximun total price was of:', list2[:5].max())  # 5 indicators
            print('The average price of the least sold pproducts is:', list2[:5].mean())
            print('The average price for all products is:', list2[:5].mean())
            print('The lowest price of the least sold pproducts is:', list2[:5].min())
            print('To see the least sold products see the graph:')
            sr = np.array(sr)
            name0 = df[df['Precio total']==list2[0]]['Nombre producto'].values
            name1 = df[df['Precio total']==list2[1]]['Nombre producto'].values
            name2 = df[df['Precio total']==list2[3]]['Nombre producto'].values
            name3 = df[df['Precio total']==list2[5]]['Nombre producto'].values
            name4 = df[df['Precio total']==list2[7]]['Nombre producto'].values
             # Start setting the graphs
            plt.bar([str(name0), str(name1) , str(name2) , str(name3) , str(name4)], [list2[0], list2[1], list2[3], list2[5], list2[7]], color=['black'])
            plt.xlabel ("Name of the product")
            plt.ylabel ("price of the product")
            plt.title ("Least sold pproducts")
            plt.show()
        elif choice == '4':
            choice = ''
            print('Enter the path to the excel file')
            df = pd.read_excel(input())  # put the path for the excel file to read
             # start defining variables
            name0 = df['Fecha de compromiso']
            name0 = np.array(name0)
            name0 = np.sort(name0)
            list1 = df['Precio total']
            list1 = np.array(list1)
            list1 = pd.DataFrame(df,columns=['Fecha de compromiso','Precio total'])  # Creates a data frame
            list1 = list1.sort_values(by='Fecha de compromiso', ascending=True)  # sorts values from dataframe 
            list2 = list1.max()
            print('The biggest sale was made on', list2['Fecha de compromiso'])  # 5 indicators
            list2 = list1.min()
            print('The smallest sale was made on:', list2['Fecha de compromiso'])
            print('The first sale made was on', name0[0])
            print('The most recent sale was made on:', name0[-1])
            print('To see the least sold products see the graph:')
             # Start setting the graphs
            plt.plot(name0, list1['Precio total'], color='#ffc0cb')
            plt.xlabel ("Date")
            plt.ylabel ("Income")
            plt.title ("Changes in sales over time")
            plt.show()
            int_choice = 4
            loop = False
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False
        else:
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]

def review():
    print('Did you like the program?')
    print('1 is for yes')
    print('2 is for no')
    x = input()
    if int(x) >= 1 and int(x) <= 1:
        print('We are happy you liked it :)')
    else:
        print('We are sorry to hear that :(')
    

def main(): #Must Access this to continue.
    print('Enter the password for iBasto ')
    p = input()
    if int(p) >= int(r) and int(p) <= int(r):
        print ('Right.  Off you go.')
        print(get_menu_choice())
        print(review())
    else:
        print ('Auuuuugh!')
        print('Wrong ppassword')

print(main())
  # Calling the menu function


