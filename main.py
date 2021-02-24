#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse Top 3 Countries that visited Singapore from 2007-2017
#Name: <Maurice>
#Group Name: <Name>
#Class: <PN2004L>
#Date: <09/02/2021>
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#import  matplotlib for graphical pie chart
import matplotlib.pyplot as pie


#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)

#CLASS Branch: End of Code



#Main Function - Europe region 2007-2017
def sortCountry(df):
  
  #Getting the spefic countries in a region, all of years and months
  Months = df[['Year', 'Month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']]
  

  #Getting the time period 2007-2017
  Year = Months.iloc[348:479]
  
  #Getting the Selected Countries
  Selected = Year[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']]
  
  #Changing all of it to numeric so it can sum correctly
  Selected = Selected.apply(pd.to_numeric)
  
  #Summing up the number of visitors from 2007-2017 in the Europe region
  Total = Selected.sum(axis=0)
  print("The following dataframe for Europe from 2007 to 2017 are read as follows: \n")
  print(Total)
  
  #Sorted into a decending order (Most to least)
  Sorted = Total.sort_values(ascending = False)
  
  #Getting the top 3 countries that visited Singapore the most
  Top3 = Sorted.head(3)
  print("\nTop3")
  print(Top3)
  
  #Sorted into acending order and getting the top 3 countries that visited Singapore the most
  ReverseSorted = Total.sort_values(ascending = True)
  Least3 = ReverseSorted.head(3)
  print('\nLeast3')
  print(Least3)

  #Making a loop for error checking and user to choose
  
  while True:
    #Adding a list of numbers that users can only enter
    NumList = [1,2,3]

    #Giving the User the options to choose
    print("\nView data in a pie chart from 2007 to 2017, Europe region that visited Singapore.\n\n1)View all countries in the Europe region that visited Singapore.\n2)View the top most 3 countires that visited Singapore.\n3)View the top least countires that visited Singapore.")
    
    #User input
    promptUser = input()
    

    #The decision part of the code and for error checking

    #User chose 1 for countries in the Europ region
    if promptUser == str(1):
      #Putting it into a list for the Europe region
      AllEurope = [' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']

      #Inputing the pie chart
      pie.pie(Total, labels = AllEurope , startangle = 90, shadow = True, autopct='%1.2f%%')
      pie.legend()
      pie.show()
      break
    
    #User chose 2 for top 3 countries that visited Singapore the most
    elif promptUser == str(2):
      #Putting it into a list for the top 3
      TopMostCountries = [' United Kingdom ', ' Germany ', ' CIS & Eastern Europe ']
      
      #Pie chart for the top 3
      pie.pie(Top3, labels = TopMostCountries, startangle = 90, shadow = True, autopct='%1.2f%%')
      pie.legend()
      pie.show()
      break

    #User chose 3 for top 3 countries that visited Singapore the least
    elif promptUser == str(3):
      #Putting the least visited countries in a least
      TopLeastCountries = [' Greece ', ' Austria ', ' Belgium & Luxembourg ']
      
      #Pie chart for least 3
      pie.pie(Least3, labels = TopLeastCountries, startangle = 90, shadow = True, autopct='%1.2f%%')
      pie.legend()
      pie.show()
      break
    
    #Error checking
    elif not promptUser in NumList:
      print('\nERROR! Please enter 1, 2 or 3')
      

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################