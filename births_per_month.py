# function creation
def month_births(lisOlis):
# empty dict creation
    births_per_month = dict()
# data set iteration
    for grami in lisOlis:
# set the appropriate column as key
        month = grami[1]
        births =grami[4]
# use an if to set the key and add values 
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births 
        else:
# set the initiator to feel values in it
            births_per_month[month] = births
# return the dictionary
    return births_per_month
     
results_birth_per_month = month_births(cdc_list)

results_birth_per_month