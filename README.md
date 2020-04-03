# Bankmapper

This webapp takes bank data, 
the left file takes a csv file without headers in the format:
date,,,Category,company,ammount

Where date, company, and ammount come from traditional bank data

and the right file, which takes a csv file with headers in the format:
Store,Category,company

The label file can initally be empty, and will generate a blank set of companies, I then put a Store with each company, where the "Store" is the keyword of the company, which can be used to idenfity the category.

For example, if the company section was VENMO PAYMENT 3342, and I wanted to categorize all venmo payments as "Work", I would put "VENMO PAYMENT" under Store, and "Work" under category. Then, when I upload the label sheet again, all venmo payments will be categorized under work.


I can repeat this process until everything is categorized.



The purpose of this webapp is to catagorize my spending, and produce a pivot table to understand my spending. 


To setup for yourself, you should be able to clone the repositiory, run pip3 install -r requirements.txt, and then run python3 application.py
