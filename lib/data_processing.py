# This module contains functions to process student data.

def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
def display_students(student_list):
    for student in student_list:

         print(format_student_data(student))