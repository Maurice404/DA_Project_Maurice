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
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

import matplotlib.pyplot as pie

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #entertimeperiod = input("Enter start of year and month. Eg. 1978Jan")



  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe for Europe from 2007 to 2017 are read as follows: \n")
  print(df)
  

  #display a specific country (Australia) in column #33
  #country_label = df.columns[20]
  #print("\n\n" + country_label + "was selected.")

  #print(df[['Year', 'Month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']])

  Months = df[['Year', 'Month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']]

  print('The months')
  print(Months)


  Year = Months.iloc[348:479]
  print('The time period from 2007-2017, Europe region')
  print(Year)
  


  Selected = Year[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']]
  print('The selected countries')
  print(Selected)
  Selected = Selected.apply(pd.to_numeric)

  #Selected = Year[[' Greece ', ' Austria ', ' Belgium & Luxembourg ']]
  #Selected = Year[[' Greece ']]

  Total = Selected.sum(axis=0)
  
  print(Total)



  Sorted = Total.sort_values(ascending = False)

  Top3 = Sorted.head(3)

  print("\nTop 3 Countries that visited Singapore")
  print(Top3)

  
  #lmao = input("\nEnter Something:")
  

  



  

  #display a sorted dataframe based on selected country
  #print(" The" + country_label + "was sorted in ascending order. \n")
  #sorted_df =df.sort_values(country_label,ascending=[0])
  #print(sorted_df)

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