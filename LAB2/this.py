import pandas as pd

# list  1 
a = [2, 3, 2.7, 3.2, 4.1] 
  
# list 2 
b = [10, 14, 12, 15, 20] 
  
# storing average of a 
av_a = sum(a)/len(a) 
  
# storing average of b 
av_b = sum(b)/len(b) 
  
# making series from list a 
a = pd.Series(a) 
  
# making series from list b 
b = pd.Series(b) 
     
# covariance through pandas method 
covar = a.cov(b)
print("covar: ", covar)



# finding covariance manually 
def covarfn(a, b, av_a, av_b): 
    cov = 0
  
    for i in range(0, len(a)): 
        cov += (a[i] - av_a) * (b[i] - av_b) 
    return (cov / (len(a)-1)) 
  
# calling function 
cov = covarfn(a, b, av_a, av_b) 
  
# printing results 
print("Results from Pandas method: ", covar) 
print("Results from manual function method: ", cov) 
