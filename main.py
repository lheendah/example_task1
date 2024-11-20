# create an application to calculate the area of a circle

PI = 3.142

def area_of_a_circle(radius):
    r = int(radius)
    return PI * r * r

area = area_of_a_circle(10)
print(area)