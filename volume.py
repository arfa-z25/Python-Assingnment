import math

def cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

# Example usage
radius = 3
height = 10
print(f"Volume of the cylinder: {cylinder_volume(radius, height):.2f} cubic units")
