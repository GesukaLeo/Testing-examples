from math import pi
def circle_Area(r):
    return pi * (r**2)


#Test function
radii = [2,0,-3,2+5j,True,"radius"]

message ="Area of circle with r = {radius} is area {area}."

for r in radii:
    A = circle_Area(r)
    print (message.format(radius=r, area=A))
