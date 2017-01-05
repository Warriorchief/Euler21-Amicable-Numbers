#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:09:22 2016

@author: christophergreen

Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an 
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
#import math ;
    
#def get_sum_proper_factors(x):
def d(x):
    factors=[];
    for i in range (1,x):
        if x%i==0:
            if i not in factors:
                factors.append(i);
    total=0;
    for p in factors:
        total+=p;
    return total;
    
amic=[];
m=2;
while m<10000:
    if d(d(m))==m and d(m)!=m:
        amic.append(m);
    m+=1;
print(amic);


added=0;
for t in amic:
    added+=t;
print('');
print(added); #--> 31626 CORRECT