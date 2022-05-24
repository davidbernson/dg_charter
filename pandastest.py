import pandas as pd
import math
import numpy as np
import geopy.distance

from us_states import states_list, states_dict

course_data = pd.read_csv('courses.csv')

print(course_data)

state_count = 0

state_list = []
course_count = []
rating_str = []
rating_list = []
high_rated_list = []
rating = False

for i in states_list:
    temp_data = course_data
    rating_str = []
    high_rated_count = 0

    # SEARCH FOR CURRENT STATE IN DATAFRAME #
    for state in course_data.index:      
        if temp_data.loc[state, "state"] == states_dict[i] and temp_data.loc[state, "holeCount"] >= 18:
            state_count += 1

            # CHECK IF RATING EXISTS #
            if math.isnan(temp_data.loc[state, "rating"]) == False:
                rating_str += [temp_data.loc[state, "rating"]]  

        # HIGH RATED CHECKER
        if temp_data.loc[state, "state"] == states_dict[i] and temp_data.loc[state, "holeCount"] >= 18 and temp_data.loc[state, "rating"] >= 4:
            high_rated_count += 1


    # STATE AVG CONSTRUCTOR #
    if len(rating_str) == 0:
        rating_list += [0] 
    else:
        rating_list += [np.mean(rating_str)]

    state_list += [str(states_dict[i])]
    course_count += [state_count]
    high_rated_list += [high_rated_count]

    state_count = 0

course_dict = {'Count' : course_count, 'Rating' : rating_list, 'High Rated' : high_rated_list}
course_df = pd.DataFrame(data=course_dict, index=state_list)
#print('Number of 18-hole (or more) disc golf courses per US state:')
print(course_df.sort_values(by=['Rating'], ascending=False))
#print(course_df)



