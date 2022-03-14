# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("employees.csv") 
print(data.head() )
# setting first name as index column 
data.set_index(["First Name"], inplace = True, 
					append = True, drop = True) 
print(data.head() )

# resetting index 
data.reset_index(inplace = True) 

# display 
print(data.head() )
