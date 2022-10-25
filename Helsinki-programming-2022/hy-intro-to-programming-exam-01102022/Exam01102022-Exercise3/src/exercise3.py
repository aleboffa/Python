# Write your solution to exercise 3 here
def convert(my_list, my_function):
    list_euros = []
    for element in my_list:
        list_euros.append(my_function(element))

    return list_euros

#####################################################
## test
if __name__=="__main__":
    def to_euro(number):
        return f'{number} €'
    my_list = [2,3,4]
    euros = convert(my_list, to_euro)
    print(euros) # Prints out: ['2 €', '3 €', '4 €']

##############################################################
# Define function
# def test_function():
#   print('Hello from test function!')

# # Function, that takes another function as a parameter
# def execute_function(my_function):

# # Calling function given as a parameter inside the function execute_function
#     my_function()
# # Now, inside the execute_function, function test_function is called
#       execute_function(test_function)
#  # Prints out 'Hello from test function!'
######################################################