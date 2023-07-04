#!/usr/bin/env python
# coding: utf-8

# ## Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.
# 
# Example:
# 
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# Output: [2, 4, 6, 8, 10]

# In[1]:


def get_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(input_list)
print(even_numbers)


# ## Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.
# 
# Example:
# 
# import time
# 
# @timer
# def my_function():
#     # Function code goes here
#     time.sleep(2)
# 
# my_function()
# 
# Output:
# "Execution time: 2.00123 seconds"

# In[2]:


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()


# ## Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns the mean (average) of the numbers. The function should calculate the mean using the sum of the numbers divided by the total count.
# 
# Example:
# 
# def calculate_mean(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     mean = total / count
#     return mean
# 
# data = [10, 15, 20, 25, 30]
# mean_value = calculate_mean(data)
# print("Mean:", mean_value)
# 
# Output:
# Mean: 20.0

# In[4]:


def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean
data = [10, 15, 20, 25, 30,80,44,99]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


# In[ ]:




