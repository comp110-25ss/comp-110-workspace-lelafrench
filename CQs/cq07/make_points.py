"""Checking my point.py methods by instantiating a new Point object."""

__author__: str = "730530237"

from CQs.cq07.point import Point

my_point: Point = Point(6.0, 8.0)
print(f"Initial Values: x - {my_point.x}, y - {my_point.y}")

my_point.scale_by(3)
print(f"After Scaling: x - {my_point.x}, y - {my_point.y}")

my_point.scale(2)
print(f"After adding new value: x - {my_point.x}, y - {my_point.y}")
