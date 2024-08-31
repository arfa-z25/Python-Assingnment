def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

# Example usage
weight = 70  # in kilograms
height = 1.75  # in meters
print(f"BMI: {calculate_bmi(weight, height):.2f}")
