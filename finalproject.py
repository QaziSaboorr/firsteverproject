import numpy as np
import matplotlib.pyplot as plt
import math

class Country:
    def __init__(self,country,region,subregion,area,population):
        self.country = country
        self.region = region
        self.subregion = subregion
        self.area = area
        self.population = population 

    def print_all_stats(self):
        print('Country:', self.country)
        print('Region: ', self.region)
        print('Sub region: ',self.subregion)
        print('Area: ', self.area, 'Sq Km')
        print('Current Population:', self.population)
    
    def threatened(self, position ,datathreatened):
        x = [int(datathreatened[position][1]),int(datathreatened[position][2]),int(datathreatened[position][3]),int(datathreatened[position][4])]
        y = (datathreatened[0][1],datathreatened[0][2],datathreatened[0][3],datathreatened[0][4])
        dict_1= dict(zip(x,y))
        self.most_threatened_specie_value = np.array([int(datathreatened[position][1]),int(datathreatened[position][2]),int(datathreatened[position][3]),int(datathreatened[position][4])]).min()
        for key, values in dict_1.items():
            if key == self.most_threatened_specie_value:
                print('One of the most threatened specie in',self.country ,'are', values, 'and there are only',key,'type of them remaining' )
    def graph_population(self,position,data):
        y_axis = list(data[position,:])
        y_axis.pop(0)
        x_axis = list(data[0,:])
        x_axis.pop(0)
        plt.plot(x_axis,y_axis,'r', markersize = 5, alpha = 1.00, label = 'Population trend')
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.xticks([0,2,5,8,11,14,17,20],['2000','2002','2005','2008','2011','2014','2017','2020'])
        plt.legend(shadow=True, loc = 'upper left')
        plt.title('Population by year')
        plt.show()
    def average(self,position,data):
        list_population = list(data[position,:])
        list_population.pop(0)
        int_list= [int(i) for i in list_population]
        mean = int(sum(int_list)/21)
        print('Average population of',self.country,'is', mean)
    def threatened_graph(self,position,threatened_data):
        list_threatened = list(threatened_data[position,:])
        list_threatened.pop(0)
        list_threatened_names = ['Plants','Fish','Birds','Mammals']    
        plt.bar(list_threatened_names,list_threatened)
        plt.ylabel('Number of species')
        plt.xlabel('Name of species')
        plt
        plt.show()

    


def main():    
    Country_data = np.genfromtxt('Country_Data-2.csv', delimiter=',',dtype = str)
    Threatened_Species = np.genfromtxt('Threatened_Species-4.csv', delimiter=',', dtype= str)
    Population_Data = np.genfromtxt('Population_Data-3.csv',delimiter=',',dtype= str)
    list_country_names = list(Country_data[:,0])
    list_country_names.pop(0)
    i = 0 # this is constant so that the while loop is never escaped and user is asked for input again and again
    print('****Welcome to stats progam*****')
    while i < 1:

        input1 = int(input('select 0 to quit and 1 to proceed:  '))
        if input1 == 0:  
                break

        if input1 == 1:
            input1 = input('For which country would you like to know the stats about?: ')
            input_Capital = str(input1).title()
            
            while input_Capital not in list_country_names:
                input1 = input('Please re-enter the name. Check for spelling and avoid abbrevations: ')
                input_Capital = str(input1).title()
            print("\n***Requested Country Statistics***\n")
            index = list_country_names.index((input_Capital))
            index += 1
            country1 = Country(input1,Country_data[index,1],Country_data[index,2],Country_data[index,3],Population_Data[index,21])
            country1.print_all_stats()
            print('What more would you like to know about',input_Capital, '? Please choose from the options below: ')
            print('Press 1 for one of the most threatened specie.')
            print('Press 2 to graph a population trend. ')
            print('Press 3 to know the average population.')
            print('Press 4 to graph threatened specie')
            input2 = input('Please input a number: ')
            if input2 == '1':
                country1.threatened(index,Threatened_Species)
            elif input2 == '2':
                country1.graph_population(index,Population_Data)
            elif input2 == '3':
                country1.average(index,Population_Data)
            elif input2 == '4':
                country1.threatened_graph(index,Threatened_Species)
        else:
            print('Please enter a correct number.')
        
    print('Thank you for using stats program.')        
    


if __name__ == '__main__':
    main()



        
    

  