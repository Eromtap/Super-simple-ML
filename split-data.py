# -*- coding: utf-8 -*-


"""
-Here split the dataset into training and test sets 

-dataset contains 3 different subspieces of iris with 50 samples each.

-each sample has the measurements of flower sepal length, sepal width and petal
 width
 
-these measurements will be used to differentiate the subspecies

-we will be using 100 random samples as our training set, then the remaining 50
 as a test set
                                                     

"""

import csv
import random



'''

Script that simply splits the Iris dataset csv into
2 random sets. I know it's ugly, I just kinda flew thru it. It works, stop 
yelling at me! Either use the already split sets that I have graciously provided,
or use this abomination of a script to make your own. It's random, so you'll have 
different sets every time, YAAAAY!

'''

def main():
    iris_dict = {}
    train_set = {}
    test_set = {}
    
    
    ## open dataset and create dict from all rows
    
    with open('iris.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        
        for row in csv_reader: 
            if row[0]  != 'Id':
                iris_dict[int(row[0])] = row[1:]    
    
    
    ## create training set dict
    
    key_list = []
    
    nums_used = [] 
    ## I don't remember why I made this empty nums_used list. 
    ## Now I'm too afraid to get rid of it and too lazy to look and see if i need it
    ## Probly not, but whatever, it's here to stay. Sue me
    
    while len(key_list) < 100:
        selection = random.randint(1, 150)
        if selection not in key_list:
            train_set[selection] = iris_dict[selection]
            key_list.append(selection)
    

            
    ## create then randomize test dict
    
    for k, v in iris_dict.items():
        if k not in key_list:
            test_set[k] = v
    
    test_list = list(test_set.items())
    random.shuffle(test_list)
    test_set = {}
    for i in test_list:
        key = i[0]
        value = i[1]
        test_set[key] = value
    
    
    ## create training set csv from training set dict
    
    with open('training.csv', 'w', newline='') as training_file:
        writer = csv.writer(training_file, delimiter=',')
        
        for k, v in train_set.items():
            writer.writerow(v)
    
    
    
    
    ## create test set csv from test set dict
    
    with open('testing.csv', 'w', newline='') as testing_file:
        writer = csv.writer(testing_file, delimiter=',')
        
        for k, v in test_set.items():
            writer.writerow(v)



if __name__ == '__main__':
    main()











