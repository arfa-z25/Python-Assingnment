def calculate_percentage(marks_obtained, total_marks):
    percentage = (marks_obtained / total_marks) * 100
    return percentage

# Example usage
marks_obtained = 450
total_marks = 500
print(f"Percentage: {calculate_percentage(marks_obtained, total_marks):.2f}%")
