# the general function
def calc_counts(data,column):
# empty dict creation    
    births_per_any_value = dict()
# data set iteration
    for index in data:
# set the appropriate columns as keys
        year = index[0]
        month = index[1]
        date_of_month = index[2]
        day_of_week = index[3]
        births = index[4]
# if column is 0 calculate births per year
        if column == 0:
            if year in births_per_any_value:
                births_per_any_value[year] =  births_per_any_value[year] + births
            else:
                births_per_any_value[year] = births
# if column is 1 calculate births per month               
        if column == 1:
            if month in births_per_any_value:
                births_per_any_value[month] =  births_per_any_value[month] + births
            else:
                births_per_any_value[month] = births
# if column is 2 calculate births per date of month                
        if column == 2:
            if date_of_month in births_per_any_value:
                births_per_any_value[date_of_month] =  births_per_any_value[date_of_month] + births
            else:
                births_per_any_value[date_of_month] = births
# if column is 3 calculate births per day of week                                    
        if column == 3:
            if day_of_week in births_per_any_value:
                births_per_any_value[day_of_week] =  births_per_any_value[day_of_week] + births
            else:
                births_per_any_value[day_of_week] = births
# return the dict    
    return births_per_any_value



cdc_year_births = calc_counts(cdc_list,0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)


print (cdc_year_births)
print ("######################################################")
print (cdc_month_births)
print ("######################################################")
print (cdc_dom_births)
print ("######################################################")
print (cdc_dow_births)
print ("######################################################")

# the reference solution of this exercise demonstrates a smarter way of doing things
# this will save memory and effort for larger dataset and calculations.
# to run uncomment the appropriate lines  

# create the function
# def calc_counts(data, column):
#create the dict
#     sums_dict = {}
# iterate into the data    
#     for row in data:
# set the column value to be a position in our dataset
#         col_value = row[column]
# set the births column to be constant 
#         births = row[4]
# use an if according to column value
#         if col_value in sums_dict:
# set this specific value as key and and the births
#             sums_dict[col_value] = sums_dict[col_value] + births
#         else:
# here we initite and feel the dict
#             sums_dict[col_value] = births
#     return sums_dict


# cdc_year_births = calc_counts(cdc_list, 0)
# cdc_month_births = calc_counts(cdc_list, 1)
# cdc_dom_births = calc_counts(cdc_list, 2)
# cdc_dow_births = calc_counts(cdc_list, 3)