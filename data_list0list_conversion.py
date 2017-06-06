# create the function read_csv with one argument
def read_csv(filename):
# open the content of the argument
    initial_op = open(filename)
# read the content of the argument
    initial_re = initial_op.read()
# split the dataset aka put it in list and "behead the first line"
# example "sakdjadadasd", "sdasds", "sadad" ----------> ["sakdjadadasd", "sdasds", "sadad"]
    string_list = initial_re.split("\n")[1:-1]
# declare the final list outside any loops to use it later
    final_list = []
    
# iterate into the general list
    for row1 in string_list:
# for each row create empty lists to store the integers later
        int_fields = []
# now we split the content into lists of lists , we already have a list
# example ["sakdjadadasd", "sdasds", "sadad"] ----------> [["sakdjadadasd"], ["sdasds"], ["sadad"]]
        string_fields = row1.split(",")
# now we iterate into the lists of lists
        for row2 in string_fields:
# we append into the int_fields the integer converted values
            int_fields.append(int(row2))
# we append these fields into the final_list , be sure that the last append has proper identation because
# if the append is outside the loop system it will be filled with the last value of the dataset
# if the append is into the body of the second loop it will cause re-append of values equal to the number of comma seperated
# fields-columns [5] till the end of the loop. (for each line iterates five times)
# gia kathe grami kani loopa 5 fores
# the proper identation is outside the second loop to store the contents only once    
        final_list.append(int_fields)
# lastly we return the final list
    return  final_list

# we create a varivable in order to call the function
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

# then we call the variable sliced to display only ten values
cdc_list[0:10]
