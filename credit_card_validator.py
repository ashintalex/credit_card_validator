# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:27:41 2022

@author: ashinalex
"""
def card_num():
    str_list = input("Enter the Credit Card Number: ")   #input single 16digit number as str
    num_list = list(str_list)                            #split single to 16 digits
    int_list = []                               
    for x in num_list:                                   #changing 16 str digits to int list 
        int_list.append(int(x))
    return num_list
    
def odd_list(card_number):
    odd_list = []                                        #the odd number list
    for count, i in enumerate(card_number):
        if count % 2 == 0:
            odd_list.append(i)
    return odd_list

def even_list(card_number):
    even_list = []                                        #the even number list
    for count, i in enumerate(card_number):
        if count % 2 == 1:
            even_list.append(int(i))
    return even_list
    
def multiply_list (num_list):                            #doubling the list 
    multiplied_list = []
    for number in num_list:
        element = int(number) * 2
        multiplied_list.append(element)
    return multiplied_list

def sum_list(num_list):
    sum_list = sum(num_list)
    return sum_list

def one_digiting(num_list):
    output_list = []
    for number in num_list:
        if int(number) > 9:
            sum_of_num = sum(int(digit) for digit in str(number))
            output_list.append(sum_of_num)
        else:
            output_list.append(int(number))
    return output_list

def check_sum(total_sum):
    if total_sum % 10 == 0:
        print('The entered number is a Credit Card')
    else:
        print('The entered card is not a Credit Card')
    
def main():
    card_number = card_num()

    even_num_list = even_list(card_number)
    sub_odd_list = odd_list(card_number)


    double_odd_list = multiply_list(sub_odd_list)
    final_odd_list = one_digiting(double_odd_list)

    even_sum = sum_list(even_num_list)
    odd_sum = sum_list(final_odd_list)
    total_sum = odd_sum + even_sum
    check_sum(total_sum)

if(__name__ == "__main__"):
    main()
    
