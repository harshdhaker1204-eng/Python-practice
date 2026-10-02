"Pratice question no 1"
from scipy import constants
# print(constants.kmh)
# print(constants.speed_of_light)
# print(constants.gravitational_constant)
# print(constants.pi)

"Pratice question no 2"
# from scipy.constants import kilo
# km=5
# meters=km*kilo
# print(meters)

# from scipy.constants import inch
# inc=10
# meters=inc*inch
# print(meters)

"pratice question no 3"
from scipy .optimize import fsolve

# def equ(x):
#     return x**2-5*x+6
# val_x=fsolve(equ,1)
# print(val_x)

from scipy .optimize import minimize_scalar

# def min_sca(x):
#     return (x-5)**2+10
# result=minimize_scalar(min_sca)
# print(result.x)
# print(result.fun)

# from scipy.integrate import quad
# def fuction(x):
#     return x**2
# result,error=quad(fuction,0,5)
# print(result)
# print(error)

interval=[[1,2],[3,4],[6,7]]
print(len(interval))