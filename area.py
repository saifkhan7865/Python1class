# first ask the input of the radius of the circle
# store the input of the circle in float 
# calculating the area of the circle

print("This is the Area calculator of Circle:")
units = input("Enter the units : ")
PIE= float(input("Enter the value of PIE: "))
Radius = float(input("Enter the value of Radius of the Circle: "))

Area_of_Circle= PIE * Radius * Radius

print(f"The area of the circle is {Area_of_Circle} {units}")