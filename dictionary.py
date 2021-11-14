#assigning a dictionary
#ascii value of a=97 and z=122 taking range in b/w them
#converting int to character by using chr() function
#adding in dictionary which is defined as d={}

d={}
for i in range(97,123):
    n=chr(i)
    d[n]=i
print(d)
