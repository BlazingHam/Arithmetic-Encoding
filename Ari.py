from collections import Counter
import numpy as np

d=['a','a','b','a',2,'b','e','e','e']                      # values used as reference for encoding the message

x=dict(Counter(d))                                         #create dictionary and count how many times they appear

print(" Dictionary values are ",x,"\n")

t=sorted(zip(x.values(), x.keys()))                        # sort and convert from dictionary values to list
y=[x/len(d) for x, char in t]                              # get probabilities of the occuring values
y.reverse()                                                # y are the probabilities of each element in d

count=0
c=[]
for i in range (len(y)):
    count=count+y[i]   
    c.append(count)                                        # c is the sum of probabilities

c.insert(0,0)                                              # insert first element as 0
c=[round(c,2) for c in c]                                  # round the values to two decimal places
count=0

z=[char for x, char in t]                                  # get the elements from the dictionary
print(" Dictionary elements are ",z)                       # z has unique dictionary elements
print(" The pmf values of the dictionary are ",c,"\n")
print()

sub=[]
c.reverse() 
for i in range (len(c)):
    count=abs(c[i]-count)
    sub.append(count)                                      # gets the difference between each consectutive probability value
    count=c[i]                                             #now c has the difference of the probabilities, which is needed for encoding
sub.remove(1.0) 
sub=[round(sub,1) for sub in sub]

m=['b',2,'a']                                              # message to be encoded

temp=c
np.array(temp)                                             # create a temp list that gets updated
new=[]
np.array(new)                                              # create new list that gets updated
np.array(z)
count=0

for w in range(len(m)-1):
    count=count+1                                          # keeps track of end of list
    for j in range(len(z)-1):
        if count==(len(m)-1):                              # once the message has ended
            ar=temp[j]
            aq=temp[j+1]
            v=temp
        if m[w]==z[j]:                                     # if the message elements matches with the dictionary
            a=temp[j]                                      # take element index that matches with the pmf and add to new
            b=temp[j+1]                                    # take next element index that matches with the pmf and add at end of new
            s=a-b                                          # factor to help in arithmetic encoding
            new.append(a)
            del temp[:]
            for q in range(len(sub)-1):
                ax=a-s*sub[q]
                new.append(ax)                             #updates new pmf to new
                a=ax
            new.append(b)
            temp=new.copy()                                # puts pmf in temp
            del new[:]
        
print(" The PMF for message ",m, " is - ",v)
print(" The range for message  ",m," is - ",ar,'-',aq)
print("\n")
               
               
                







