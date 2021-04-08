'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

#!/usr/bin/python

height = 5
radius = 3.14

def get_volume(height, radius):
    return radius**2 * 3.14592 * height

def get_surface_area(height, radius):
    return 2*3.14592 * radius * height

print(f"For a cylinder with height:{height} and radius:{radius}")
print(f"Volume = {get_volume(height, radius)}")
print(f"Surface Area = {get_surface_area(height, radius)}")
