# function creation
def dow_births(lisOlis_data):
# empty dict creation    
    births_per_day = dict()
# data set iteration
    for row in lisOlis_data:
# set the appropriate column as key
        day = row[3]
        births = row[4]
# use an if to set the key and add values
        if day in births_per_day:
            births_per_day[day] = births_per_day[day] + births
        else:
# set the initiator to feel values in it
            births_per_day[day] = births
# return the dictionary
    return births_per_day

results_births_per_day = dow_births(cdc_list)

results_births_per_day