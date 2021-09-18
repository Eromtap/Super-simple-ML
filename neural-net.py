
"""

-dataset contains 3 different subspieces of iris with 50 samples each.

-each sample has the measurements of flower sepal length, sepal width and petal
length and petal width
 
-these measurements will be used to differentiate the subspecies

-we will be using 100 random samples as our training set, then the remaining 50
 as a test set
 
-Algorithm should be pretty straight forward, though IDK how well it will work

-I intend to have each measurement act as both input and weighted node

-this may or may not be such a good thing with only 4 inputs, but may be very 
 effective for a set with dozens or hundreds of inputs
 
-basically, all the weights will be random between 0 and 1 at first (may use
 different range) and then a round of training will be started.

-there will be 10 rounds of training before any change to weights and between 
 each change
 
-changes will be made in an incremental fashion. Starting with the first "node"

-After 10 training runs, the first node weight will be increased by a set amount
 potentially .1 or .01 or something even smaller. 
 
-then another 10 runs to see if that improved accuracy or degraded it.

-if improved, change will remain. if degraded, change will be reversed, so
 weight will change to -.1 or whatever. 
 
-if still degraded, it will go back to what it was (in the beggining, or at 
 whatever step we're at) and we move to the next node and repeat

-this will continue until an acceptable lvl of accuracy is achieved

-starting out, I'd be happy with anything over 75%, we can improve from there                                                    

"""





"""

how do we get a value to represent one of 3 choices of flower? do we set the 
values? do we let it decide?????????????????????????????????????????????????????????????????????

Leaning towards letting it decide. we need to start with a random prediction, then somehow let it apply values to each flower
how do we start random, then make it choose not randomly???

maybe start with each flower having a value. maybe -1, 0 and 1. then once we have the sum of the node values, make predictions based on
which value is closest. then once it is wrong a lot of the time, change those values or change the weights to closer match them. 
now i may have talked myself into setting flower values....idk


"""


import csv
import random




while 1:
    
    ## just a counter to keep track of our correct predictions
    
    correct = 0

    
    
    '''
    Below is the node and weight section. The first section where nodes equal a random number between -1 and 1
    is used to let the machine try random weights until a satisfactory set is found
    
    The next block is to copy and paste the weights to give them static values.
    basically comment out one block to use the other. It's ugly, but it works
    
    As you can see, I abandoned my idea of incrementing the weights. This works
    too well using random weights for me to bother with incrementing. I still
    think it could be a good idea and will be exploring it more
    
    '''
    
    
    
    # Block for generating random weights ##############
    
    # sl_node = round(random.uniform(-1, 1), 4) 
    # sw_node = round(random.uniform(-1, 1), 4)
    # pl_node = round(random.uniform(-1, 1), 4)
    # pw_node = round(random.uniform(-1, 1), 4)
    
    
    
    
    # Block for setting static weights ##################
    
    sl_node = 0.0206  # 98%% correct in training with these weights
    sw_node = -0.016
    pl_node = -0.0172
    pw_node = 0.3804
        
        
        
     ## Giant space so the blocks where you're supposed to tinker around are nice and far from other stuff   
        
        
        

    # func to add up weighted nodes and input values    
    def nodes(sep_len, sep_wid, pet_len, pet_wid):

        return (sep_len * sl_node) + (sep_wid * sw_node) \
            + (pet_len * pl_node) + (pet_wid * pw_node)
            
    '''
    subspecies values
    Iris-virginica = .66 to 1
    Iris-versicolor = .33 to .66
    Iris-setosa= 0 to .33
    
    I gave them pretty arbitrary values. Started with -1, 0 and 1. Ended up
    deciding on these ranges. Mostly because it wasnt working before the change,
    but I figured out it wasnt the values, it was another issue. So play around
    with these values if you want, just remember to change them below in the for
    loop
    '''
    
    ## Pretty straight forward here, open the csv file and assign the values
    ## of length, width, etc to variables and call the nodes func to do the 
    ## math. Then assign a prediction based on the range the resulting math 
    ## falls into. Change the file name to switch between training and test sets
    
    with open('testing.csv') as file: ## This file name here......
        
        csv_reader = csv.reader(file, delimiter=',')
        
        for row in csv_reader: 
            sep_len = float(row[0])
            sep_wid = float(row[1])
            pet_len = float(row[2])
            pet_wid = float(row[3])
            species = row[4]
            
            #this block is where the species values matter
            
            if nodes(sep_len, sep_wid, pet_len, pet_wid) > .66:  
                prediction = 'Iris-virginica'
            elif nodes(sep_len, sep_wid, pet_len, pet_wid) < .66\
                and nodes(sep_len, sep_wid, pet_len, pet_wid) > .33:
                    prediction = 'Iris-versicolor'
            elif nodes(sep_len, sep_wid, pet_len, pet_wid) < .33\
                and nodes(sep_len, sep_wid, pet_len, pet_wid) > 0:
                prediction = 'Iris-setosa'
                
            else:
                prediction = ''
            
            if prediction == species:
                correct += 1
            else:
                answer = ''

            

    
    '''
    
    Ok, so this if statement below is just to break out of the main while loop
    when it hits a level of accuracy that we set. for a training set of 100,
    set it to say 80 or 90. Or lower if you want, I don't judge. Then, obviously,
    for a test set of say 50, you have to set it lower because all this does is
    break out of the loop when the correct counter (remember that guy from the top)
    hits the number you set. You cant set it higher than the number of rows in
    the dataset or, you know, it'll never get there lol. Yeah yeah, i could have
    made it percentage based by simply dividing corect answers by the number of rows,
    but I'm tired and can't be bothered. you can do it if you want, would make 
    it easier to use.
    
    '''
            
     
    if correct > 40: ## this guy right here, change this num to adjust accuracy target
        break
    
    
'''

Ok, here we have adjusted the weights randomly and found a set that beats our
accuracy target from above (or we used static weights that we already knew would beat it)
and we have broken out of the loop. Below, we print the number of correct predictions
and then the weights that gave us those delicious predictions. This way, you can
copy and paste them into the static weight block above and use them over and over 
to your little heart's content. They'll work on the test or training set (obviously,
that's kind of the point. Did I mention I was tired?)

they print in the order in which they should be copied/pasted. They're also labeled, 
so if you screw it up, dont blame me!

'''
print(correct, '\nsl_node: ', sl_node, '\nsw_node: ', sw_node, '\npl_node: ', pl_node, '\npw_node: ', pw_node)










































