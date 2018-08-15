"""
This program compute the area of a square,triangle and trapezium
and display result
"""
#Area of a square
#Input length
print('This program calculate Area of a Square\n')
length = int(input('Enter square length(cm): '))
#calculate Area
area = length * length
#print result
print('The area of the square with length',length,'cm is ',area,'\n')

#Area of a triangle
#Input breadth
print('This program calculate Area of a Triangle\n')
breadth = int(input('Enter value for breadth: '))
#Input height
height = int(input('Enter value for height: '))
area = 1/2 * breadth * height
#print result
print('The area of the triangle',area,'\n')

#Area of a trapezium
#Input first side
print('This program calculate Area of a Trapezium\n')
a = int(input('Enter value for side1 : '))
#Input second side
b = int(input('Enter value for side2 : '))
#Input height
height = int(input('Enter value for height: '))
area = 1/2 * (a+b) * height
#print result
print('The area of the trapezium',area)
