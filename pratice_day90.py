"Pratice question no 1"
from scipy.optimize import fsolve
def equations(values):
    x,y=values
    eq1=x+y-10
    eq2=x-y-2
    return [eq1,eq2]
solution=fsolve(equations,[0,0])
print(solution)

"Pratice question no 2"
from scipy.stats import norm
mean=50
std=10

#Probability X=60
p1=norm.cdf(60,mean,std)
print("P(X<60)=",p1)

#Probability 40<x<60
p2=norm.cdf(60,mean,std)-norm.cdf(40,mean,std)
print("P(40<X<60)=",p2)
