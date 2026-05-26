# Smart Employee ID Generator

employee_name = input("Enter Employee Name: ")
joining_year = input("Enter Joining Year: ")
department_name = input("Enter Department Name: ")

name_part = employee_name[:3].upper()
year_part = joining_year[-2:]
department_part = department_name[:3].upper()

employee_id = name_part + year_part + department_part

print("Generated Employee ID :", employee_id)