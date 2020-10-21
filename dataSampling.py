# IMPORT LIBRARIES
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv


# RAED CSV FILE
df = pd.read_csv('data2.csv')

data = df["average"].tolist()

# GET MEAN AND STANDARD DEVIATION FOR TOTAL DATA
pop_mean = statistics.mean(data)
print("MEAN OF TOTAL DATA IS")
print(pop_mean)

std_deviation = statistics.stdev(data)
print("STANDARD DEVIATION OF TOTAL DATA IS")
print(std_deviation)


#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.show()

# CODE TO FIND MEAN AND STANDARD DEVIATION FOR RANDOM 100 DATA POINTS
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    
#STD_DEVIATION = statistics.stdev(dataset)
#print("STD_DEVIATION OF SAMPLE DATA IS")
#print(STD_DEVIATION)



# FUNCTION TO PLOT MEAN OF GRAPH

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("MEAN OF SAMPLING DISTRIBUTION",mean)
    
    
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.show()



# FUNCTION TO GET MEAN OF 100 DATA POINTS 1000 TIMES AND PLOT THE GRAPH

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)

# CALL SETUP
setup()

# FUNCTION FOR STANDARD DEVIATION OF GRAPH
def standard_deviation():
    mean_List = []
    for i in range(0,1000):
        set_of_Mean = random_set_of_mean(100)
        mean_List.append(set_of_Mean)

    std_deviation = statistics.stdev(mean_List)
    print("STANDARD DEVIATION OF SAMPLING DISTRIBUTION",std_deviation)

# CALL STD_D FUNCTION
standard_deviation()

# FORMULA OF SAMPLING DATA
#Standard deviation of sampling mean distribution = Standard Deviation of Population / sqrt (number of data in each sample)







