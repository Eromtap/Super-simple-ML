# Super-simple-ML
I made a machine learning thing to help those who may be struggling.

OK, so heres the deal. I've been working with ML for awhile. Ive used Numpy, Pandas, Scikit learn, tensor etc and something occured to me....
I've never actually written a machine learing algorithm from scratch. Just for fun, I decided to give it a go.
In doing so, i wanted to create something simple that anyone struggling to understand the concepts could grasp and hopefully help them along.
In this project, there is no calculus, no back propogation, no linear algebra. In fact, the only python libraries used are random and csv, not even pandas shows up.
The only math is some simple addition and multiplication. I purposly avoided arrays as well, and instead opted to keep the data in the csv files and utilize it from there. 
I also wanted to see if I could create something in which the inputs acted as both inputs and weighted nodes and make it work.
No hidden layers whatsoever and to my surprise, it actually works!
I dont know if one could really call this a neural network, but thats what I called it and it's staying lol. It is undoubtedly machine learning however.
I was surprised at how simple I could make this project and have it actually work. Hell, I think there are more lines of comment than code! It's not elegant, it's not pretty, but dammit it works.
For anyone wanting to get a handle on some of the basic principles of ML and doing so in the absolute simplest way imaginable, I encourage you to check this out.
While this is a simple project, I found that I quite like some of the things I stumbled on and am going to explore them further.
I left all my notes and frustrated comments in the code. I hope these will serve to both enlighten and entertain. They clearly show my thought processes.

Included are 5 files. 3 datasets, one is the standard Iris* set called Iris.csv, then I have included 2 csv files that are just that set split into training and test sets.
These are conviniently called traingin.csv and testing.csv. Then I included a file called split-data.py, use this if you want to split the Iris set yourself into training and testing. Last is where the magic happens, neural-net.py.

Oh, I realized I use the term weights in the comments a lot. For anyone just learning, weights are just the amount of emphasis we put on each node value. So if the machine decides that a certain input leads to better predictions than another, it will weight that input (or node, again in this project they are one in the same) more. Now this program chooses weights completely at random, but the same principle applies, it just doesnt back propogate to find a nice set of weights, it stumbles into them. You may hear the term bias thrown around. There are no biases in this project, didn't need any.

Lastly, I am open to any questions / comments. Also, plese read all comments before using the program, they explain exactly what to do and how to do it. 

Enjoy!

* The iris dataset is explained here, credit Wikipedia  https://en.wikipedia.org/wiki/Iris_flower_data_set.  But in short, it's a set of 150 iris flowers of 3 different sub species. There are 50 examples of each subspecies with thier corresponding physical measurements. The object is to randomize the samples and see how accurately a machine can predict which subspecies a flower is based soley on these measurements and how often it predicts correctly. It's harder than it sounds, these subspecies are very close to one another in size and there is a significant amount of overlap in the measurements. This is a very common dataset for ML because it is small and its characteristics are well understood. It's basically the one everybody first learn on which is one of the reasons I used it here.

PS. Please excuse grammer and spelling mistakes. It's 1:34 AM and I'm tired. I may fix them later.


PPS. No, I wont...Let's be honest.
