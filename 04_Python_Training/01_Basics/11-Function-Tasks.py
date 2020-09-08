# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    # Code Here
    int_sum = n1 + n2

    if int_sum == 10:
        print(True)
    else:
        print(False)

check_ten(5,5)
check_ten(5,6)

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    # Code Here
    int_sum = n1 + n2

    if int_sum == 10:
        print(True)
    else:
        print(int_sum)

check_ten_sum(4,6)
check_ten_sum(5,6)


# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    # Code Here
    print(mystring[0].upper())

first_upper('hello')

# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def last_two(mystring):
    # Code Here
    if len(mystring) > 2:
        print(mystring[-2:])
    else:
        print('Error')

last_two('python')
last_two('hi')

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

def seq_check(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


seq_check([1,2,3])

seq_check([7,7,7,1,2,3,7,7,7])

seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3])

# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    # Code Here
    print(abs(len(s1) - len(s2)))

compare_len('Denis','Cooper')


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):

    # Code Here
    if len(mylist)%2 == 0:
        print(sum(mylist))
    else:
        print(max(mylist))


sum_or_max([1,5,7,9,10])
sum_or_max([1,5,7,10])