# Bankmapper

This webapp takes bank data, 
the left file takes a csv file without headers in the format:
date,,,Category,company,ammount

Where date, company, and ammount come from traditional bank data

and the right file, which takes a csv file with headers in the format:
Store,Category,company

The label file can initally be empty, and will generate a blank set of Stores, I then put a category with each store, once for each store, and upload the label_download and updateable_dataset files. I can repeat this process until everything is categorized



The purpose of this webapp is to catagorize my spending, and produce a pivot table to understand my spending. 


To setup for yourself, you should be able to clone the repositiory, run pip3 install -r requirements.txt, and then run python3 application.py
