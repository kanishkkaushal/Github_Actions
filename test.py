#this a python program to see if github actions can build this code and run the test

#Program to see if list has a multiple of 5

given_list = [1,2,3,100,55,0]
given_list1 = [1,2,3,76,32]

def multiple_of_five_finder(arr):
    for a in arr:
        if a % 5 == 0:
            return True
    return False

# def test_multi():
#     assert multiple_of_five_finder([1,2,3,100,55,0]) == True
#     assert multiple_of_five_finder([1,2,3,76,32]) == False

