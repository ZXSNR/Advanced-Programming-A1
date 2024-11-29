import tkinter as tk
from tkinter import ttk

def load_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 6:
                student_no, name, coursework1, coursework2, coursework3, exam_score = parts
                students.append({
                    'student_no': student_no,
                    'name': name,
                    'coursework1': int(coursework1),
                    'coursework2': int(coursework2),
                    'coursework3': int(coursework3),
                    'exam_score': int(exam_score)
                })
    return students

students = load_student_data('studentMarks.txt')

def calculate_grades(students):
    for student in students:
        total_coursemark = student['coursework1'] + student['coursework2'] + student['coursework3']
        student['total_coursemark'] = total_coursemark
        total_score = total_coursemark + student['exam_score']
        student['total_percentage'] = (total_score / 160) * 100
        if student['total_percentage'] >= 70:
            student['grade'] = 'A'
        elif student['total_percentage'] >= 60:
            student['grade'] = 'B'
        elif student['total_percentage'] >= 50:
            student['grade'] = 'C'
        elif student['total_percentage'] >= 40:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'

def calculate_summary(students):
    num_students = len(students)
    average_percentage = sum(student['total_percentage'] for student in students) / num_students if num_students > 0 else 0
    return num_students, average_percentage

def update_table(view):
    for row in table.get_children():
        table.delete(row)
    
    if view == "All Students":
        filtered_students = students
    elif view == "High Score":
        filtered_students = sorted(students, key=lambda x: x['total_percentage'], reverse=True)[:1]
    elif view == "Low Score":
        filtered_students = sorted(students, key=lambda x: x['total_percentage'])[:1]
    else:
        filtered_students = [student for student in students if student['name'] == view]
    
    for student in filtered_students:
        table.insert('', 'end', values=(
            student['name'],
            student['student_no'],
            student['total_coursemark'],
            student['exam_score'],
            f"{student['total_percentage']:.2f}%",
            student['grade']
        ))
    
    num_students, avg_percentage = calculate_summary(filtered_students)
    summary_label.config(text=f"Number of Students: {num_students} | Average Percentage: {avg_percentage:.2f}%")

root = tk.Tk()
root.title("Student Manager")
root.geometry("900x500")
root.resizable(False, False)

label = tk.Label(root, text="Student Manager", font=('Helvetica', 16, 'bold'))
label.grid(row=0, column=0, columnspan=5, pady=10)

control_frame = tk.Frame(root)
control_frame.grid(row=1, column=0, columnspan=5, pady=10)

view_label = tk.Label(control_frame, text="View: ", font=('Helvetica', 12))
view_label.grid(row=0, column=0, padx=5)

view_options = ["All Students", "High Score", "Low Score"] + [student['name'] for student in students]
view_dropdown = ttk.Combobox(control_frame, values=view_options, state="readonly", font=('Helvetica', 12), width=30)
view_dropdown.set(view_options[0])
view_dropdown.grid(row=0, column=1, padx=5)

view_button = tk.Button(control_frame, text="Show", command=lambda: update_table(view_dropdown.get()), font=('Helvetica', 12), width=10)
view_button.grid(row=0, column=2, padx=5)

columns = ('Name', 'Number', 'Total Coursework', 'Exam Mark', 'Overall Percentage', 'Grade')
table = ttk.Treeview(root, columns=columns, show="headings", height=12)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=140)
table.grid(row=2, column=0, columnspan=5, padx=25)

summary_label = tk.Label(root, text="", font=('Helvetica', 12))
summary_label.grid(row=3, column=0, columnspan=5, pady=20)

button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=5)

view_all_button = tk.Button(button_frame, text="View All", command=lambda: update_table("All Students"), font=('Helvetica', 12), width=12)
view_all_button.grid(row=0, column=0, padx=50)

high_score_button = tk.Button(button_frame, text="High Score", command=lambda: update_table("High Score"), font=('Helvetica', 12), width=12)
high_score_button.grid(row=0, column=1, padx=50)

low_score_button = tk.Button(button_frame, text="Low Score", command=lambda: update_table("Low Score"), font=('Helvetica', 12), width=12)
low_score_button.grid(row=0, column=2, padx=50)

calculate_grades(students)
update_table("All Students")

root.mainloop()
