########################################################################
##      TASK 1 - Load CSV with NumPy + Pandas + Visualization         ##
## * Use NumPy to load the CSV.TAAS * Print the shape (rows, columns) ##
########################################################################

## Import ##
#import numpy as np

#data = np.genfromtxt('/WeeklyFolder/login_activity.csv', delimiter=',')
#print(data.shape)

########################################################################
##      TASK 2 - Load CSV with Pandas (Preview First 10 Rows          ##
## * Use Pandas to load the CSV * Print the first 10 rows (head(10))  ##
########################################################################

## Import ##
#import pandas as pd

#data = pd.read_csv('/WeeklyFolder/login_activity.csv')
#print(data.head(10))

#####################################################################
##              TASK 3 - Filter Failed Logins Only                 ##
## *Filter rows where LoginResult == 'Failed'                      ##
## * Display a small sample of filtered results example: head(10)) ##
#####################################################################

## Import ##
#import pandas as pd
#data = pd.read_csv('/WeeklyFolder/login_activity.csv')

#failedx = data[data['LoginResult'] == 'Failed']
#print(failedx.head(10))

###########################################################################
##                   TASK 4 - Count Failed Logins by IP Address          ##
##           * Group by IPAddrress * Count failed attempts per IP        ##
## * Print the resulting counts (or print top results soreted descending ##
###########################################################################

## Import ##
#import pandas as pd
#data = pd.read_csv('/WeeklyFolder/login_activity.csv')
#ipx = data.groupby('IPAddress')['LoginResult'].value_counts()
#print(ipx.head(10))

###########################################################################
##              TASK 5 - Create a Bar Chart of Failed Logins per IP      ##
##           * Create a bar chart of failed login counts per IP          ##
##           * Label axes and include a title                            ##
###########################################################################

## Import ##
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/WeeklyFolder/login_activity.csv')
failedx = data[data['LoginResult'] == 'Failed']
ipx = failedx['IPAddress'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(ipx.index, ipx.values, color='green')
plt.title('Failed Logins per IP Address')
plt.xlabel('IP Address')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
