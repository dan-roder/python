# checking types
# print(type(5) == int)

# student = {'first_name' : 'Dan'}

# print(student['first_name'])
import math

def printing_function(str):
  print(str)

def area_of_circle(radius):
  PI = math.pi

  circumference = 2 * PI * radius
  print('The circumference is equal to:', circumference)

  area = PI * (radius ** 2)
  print('The area is:', area)
  print()


area_of_circle(3)

area_of_circle(6)