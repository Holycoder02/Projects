import tkinter as tk
from tkinter import messagebox, simpledialog

student_grade = {}

class StudentGradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Management System")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Title
        title_label = tk.Label(root, text="Student Grade Management System", 
                              font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=15)
        
        # Buttons Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Add Student", command=self.add_student, 
                 width=20, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=5)
        tk.Button(button_frame, text="Update Student Grade", command=self.update_student, 
                 width=20, bg="#2196F3", fg="white", font=("Arial", 10)).pack(pady=5)
        tk.Button(button_frame, text="Delete Student", command=self.delete_student, 
                 width=20, bg="#f44336", fg="white", font=("Arial", 10)).pack(pady=5)
        tk.Button(button_frame, text="View All Students", command=self.view_students, 
                 width=20, bg="#FF9800", fg="white", font=("Arial", 10)).pack(pady=5)
        tk.Button(button_frame, text="Exit", command=root.quit, 
                 width=20, bg="#9C27B0", fg="white", font=("Arial", 10)).pack(pady=5)
        
        # Text area for displaying students
        text_label = tk.Label(root, text="Student List:", font=("Arial", 12, "bold"), 
                             bg="#f0f0f0", fg="#333333")
        text_label.pack(anchor="w", padx=20)
        
        self.text_area = tk.Text(root, height=12, width=70, font=("Arial", 10))
        self.text_area.pack(pady=10, padx=20)
        
        # Display initial message
        self.text_area.insert(tk.END, "No students yet. Click 'View All Students' to see the list.")
    
    def add_student(self):
        name = simpledialog.askstring("Add Student", "Enter student name:")
        if name:
            if name in student_grade:
                messagebox.showwarning("Warning", f"{name} already exists!")
                return
            grade = simpledialog.askinteger("Add Student", "Enter student grade (0-100):")
            if grade is not None:
                if 0 <= grade <= 100:
                    student_grade[name] = grade
                    messagebox.showinfo("Success", f"Added {name} with grade {grade}")
                    self.view_students()
                else:
                    messagebox.showerror("Error", "Grade must be between 0 and 100!")
    
    def update_student(self):
        name = simpledialog.askstring("Update Student", "Enter student name:")
        if name:
            if name in student_grade:
                grade = simpledialog.askinteger("Update Student", "Enter new grade (0-100):")
                if grade is not None:
                    if 0 <= grade <= 100:
                        student_grade[name] = grade
                        messagebox.showinfo("Success", f"Updated {name}'s grade to {grade}")
                        self.view_students()
                    else:
                        messagebox.showerror("Error", "Grade must be between 0 and 100!")
            else:
                messagebox.showerror("Error", f"{name} not found!")
    
    def delete_student(self):
        name = simpledialog.askstring("Delete Student", "Enter student name to delete:")
        if name:
            if name in student_grade:
                del student_grade[name]
                messagebox.showinfo("Success", f"{name} has been deleted")
                self.view_students()
            else:
                messagebox.showerror("Error", f"{name} not found!")
    
    def view_students(self):
        self.text_area.delete(1.0, tk.END)
        if student_grade:
            self.text_area.insert(tk.END, "Name".ljust(30) + "Grade\n")
            self.text_area.insert(tk.END, "-" * 40 + "\n")
            for name, grade in student_grade.items():
                self.text_area.insert(tk.END, f"{name}".ljust(30) + f"{grade}\n")
        else:
            self.text_area.insert(tk.END, "No students found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGradeApp(root)
    root.mainloop()