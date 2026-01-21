"""Write a Python script that checks whether a triangle is equilateral, isosceles, or scalene.
Prompt the user to enter the lengths of the three sides.

Triangle Types:

Equilateral: All three sides are equal.

Isosceles: Two sides are equal.

Scalene: All sides are different.

Input: Enter the lengths of the triangle sides:

x: 6

y: 8

z: 12

Output: Scalene triangle."""

side_1 = input("Enter the 1st side of the triangle ")
side_2 = input("Enter the 2nd side of the triangle ")
side_3 = input("Enter the 3rd side of the triangle ")

if side_1 == side_2 == side_3:
    print("Eduilateral triangle")
elif (side_1 == side_2 or side_1 == side_3 or side_2 == side_3):
    print("isosceles triangle")
elif side_1 != side_3 and side_1 !=side_2 and side_3 != side_2:
    print("scalene triangle")
