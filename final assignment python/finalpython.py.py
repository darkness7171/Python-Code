import csv
import tkinter as tk
from tkinter import messagebox

# Credentials for login
credentials = {'username': 'admin', 'password': 'admin123'}

# Fields for student data
student_fields = ['roll', 'name', 'age', 'email', 'phone']

# File paths for databases
student_database = 'user.txt'
grade_database = 'grades.txt'
eca_database = 'eca.txt'

# Function to create login window
def login_window():
    # Creating Tkinter window for login
    login_window = tk.Tk()
    login_window.title("Login")

    # Function to handle login attempt
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == credentials['username'] and password == credentials['password']:
            messagebox.showinfo("Login Successful", "Login successful!")
            login_window.destroy()
            main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # Username entry field
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    # Password entry field
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    # Login button
    login_button = tk.Button(login_window, text="Login", command=handle_login)
    login_button.pack()

    login_window.mainloop()

# Function to create main menu window
def main_menu():
    # Creating Tkinter window for main menu
    main_menu = tk.Tk()
    main_menu.title("Student Database Management System")

    # Function to handle menu choices
    def handle_choice(choice):
        if choice == 'Add New Student':
            add_student_window()
        elif choice == 'View Students':
            view_students_window()
        elif choice == 'Search Student':
            search_student_window()
        elif choice == 'Update Student':
            update_student_window()
        elif choice == 'Delete Student':
            delete_student_window()
        elif choice == 'Add Grades':
            add_grades_window()
        elif choice == 'View Grades':
            view_grades_window()
        elif choice == 'Add ECA':
            add_eca_window()
        elif choice == 'View ECA':
            view_eca_window()
        else:
            main_menu.destroy()

    choices = [
        "Add New Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student",
        "Add Grades",
        "View Grades",
        "Add ECA",
        "View ECA",
        "Quit"
    ]

    # Creating buttons for menu choices
    for choice in choices:
        button = tk.Button(main_menu, text=choice, command=lambda c=choice: handle_choice(c))
        button.pack()

    main_menu.mainloop()

# Add New Student Window
def add_student_window():
    # Creating Tkinter window for adding new student
    add_student_window = tk.Tk()
    add_student_window.title("Add New Student")

    # Function to save student data
    def save_student():
        student_data = [roll_entry.get(), name_entry.get(), age_entry.get(), email_entry.get(), phone_entry.get()]
        save_student_data(student_data)
        messagebox.showinfo("Success", "Student added successfully")
        add_student_window.destroy()

    # Entry fields for student data
    roll_label = tk.Label(add_student_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(add_student_window)
    roll_entry.pack()

    name_label = tk.Label(add_student_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(add_student_window)
    name_entry.pack()

    age_label = tk.Label(add_student_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(add_student_window)
    age_entry.pack()

    email_label = tk.Label(add_student_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(add_student_window)
    email_entry.pack()

    phone_label = tk.Label(add_student_window, text="Phone:")
    phone_label.pack()
    phone_entry = tk.Entry(add_student_window)
    phone_entry.pack()

    save_button = tk.Button(add_student_window, text="Save", command=save_student)
    save_button.pack()

    add_student_window.mainloop()

# View Students Window
def view_students_window():
    # Creating Tkinter window for viewing students
    view_students_window = tk.Tk()
    view_students_window.title("View Students")
    view_students_window.geometry("800x600")  # Increase window size

    students_list = tk.Listbox(view_students_window, width=100, height=30)  # Increase listbox size
    students_list.pack()

    # Populate listbox with student data
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            students_list.insert(tk.END, " | ".join(row))

    view_students_window.mainloop()

# Search Student Window
def search_student_window():
    # Creating Tkinter window for searching student
    search_student_window = tk.Tk()
    search_student_window.title("Search Student")

    # Function to search student
    def search_student():
        roll = roll_entry.get()
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == roll:
                    messagebox.showinfo("Student Found", "Name: {}\nAge: {}\nEmail: {}\nPhone: {}".format(row[1], row[2], row[3], row[4]))
                    return
            messagebox.showinfo("Student Not Found", "Student with roll {} not found.".format(roll))

    roll_label = tk.Label(search_student_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(search_student_window)
    roll_entry.pack()

    search_button = tk.Button(search_student_window, text="Search", command=search_student)
    search_button.pack()

    search_student_window.mainloop()

# Update Student Window
def update_student_window():
    # Creating Tkinter window for updating student
    update_student_window = tk.Tk()
    update_student_window.title("Update Student")

    # Function to update student data
    def update_student():
        roll = roll_entry.get()
        updated_data = [name_entry.get(), age_entry.get(), email_entry.get(), phone_entry.get()]
        rows = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == roll:
                    rows.append(updated_data)
                else:
                    rows.append(row)
        with open(student_database, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        messagebox.showinfo("Success", "Student with roll {} updated successfully.".format(roll))
        update_student_window.destroy()

    roll_label = tk.Label(update_student_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(update_student_window)
    roll_entry.pack()

    name_label = tk.Label(update_student_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(update_student_window)
    name_entry.pack()

    age_label = tk.Label(update_student_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(update_student_window)
    age_entry.pack()

    email_label = tk.Label(update_student_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(update_student_window)
    email_entry.pack()

    phone_label = tk.Label(update_student_window, text="Phone:")
    phone_label.pack()
    phone_entry = tk.Entry(update_student_window)
    phone_entry.pack()

    update_button = tk.Button(update_student_window, text="Update", command=update_student)
    update_button.pack()

    update_student_window.mainloop()

# Delete Student Window
def delete_student_window():
    # Creating Tkinter window for deleting student
    delete_student_window = tk.Tk()
    delete_student_window.title("Delete Student")

    # Function to delete student
    def delete_student():
        roll = roll_entry.get()
        rows = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == roll:
                    continue
                rows.append(row)
        with open(student_database, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        messagebox.showinfo("Success", "Student with roll {} deleted successfully.".format(roll))
        delete_student_window.destroy()

    roll_label = tk.Label(delete_student_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(delete_student_window)
    roll_entry.pack()

    delete_button = tk.Button(delete_student_window, text="Delete", command=delete_student)
    delete_button.pack()

    delete_student_window.mainloop()

# Add Grades Window
def add_grades_window():
    # Creating Tkinter window for adding grades
    add_grades_window = tk.Tk()
    add_grades_window.title("Add Grades")

    # Function to save grades
    def save_grades():
        roll = roll_entry.get()
        grade_data = [
            ('Nepali', nepali_entry.get()),
            ('Math', math_entry.get()),
            ('Science', science_entry.get()),
            ('English', english_entry.get()),
            ('Computing', computing_entry.get()),
        ]  # Example fields
        save_grade_data(roll, grade_data)
        messagebox.showinfo("Success", "Grades added successfully")
        add_grades_window.destroy()

    roll_label = tk.Label(add_grades_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(add_grades_window)
    roll_entry.pack()

    nepali_label = tk.Label(add_grades_window, text="Nepali Grade:")
    nepali_label.pack()
    nepali_entry = tk.Entry(add_grades_window)
    nepali_entry.pack()

    math_label = tk.Label(add_grades_window, text="Math Grade:")
    math_label.pack()
    math_entry = tk.Entry(add_grades_window)
    math_entry.pack()

    science_label = tk.Label(add_grades_window, text="Science Grade:")
    science_label.pack()
    science_entry = tk.Entry(add_grades_window)
    science_entry.pack()

    english_label = tk.Label(add_grades_window, text="English Grade:")
    english_label.pack()
    english_entry = tk.Entry(add_grades_window)
    english_entry.pack()

    computing_label = tk.Label(add_grades_window, text="Computing Grade:")
    computing_label.pack()
    computing_entry = tk.Entry(add_grades_window)
    computing_entry.pack()


    save_button = tk.Button(add_grades_window, text="Save", command=save_grades)
    save_button.pack()

    add_grades_window.mainloop()

# View Grades Window
def view_grades_window():
    # Creating Tkinter window for viewing grades
    def delete_grade():
        selected_index = grades_list.curselection()
        if selected_index:
            selected_grade = grades_list.get(selected_index)
            roll, *grades = selected_grade.split(" | ")
            with open(grade_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = [row for row in reader if row and row[0] != roll]
            with open(grade_database, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            messagebox.showinfo("Success", "Grade for student with roll {} deleted successfully.".format(roll))
            view_grades_window.destroy()
            view_grades_window()

    view_grades_window = tk.Tk()
    view_grades_window.title("View Grades")

    grades_list = tk.Listbox(view_grades_window, width=80, height=20)
    grades_list.pack(padx=10, pady=10)

    # Populate listbox with grade data
    with open(grade_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            grades_list.insert(tk.END, " | ".join(row))

    delete_button = tk.Button(view_grades_window, text="Delete Selected Grade", command=delete_grade)
    delete_button.pack()

    view_grades_window.mainloop()

# Add ECA Window
def add_eca_window():
    # Creating Tkinter window for adding ECA
    add_eca_window = tk.Tk()
    add_eca_window.title("Add ECA")

    # Function to save ECA
    def save_eca():
        roll = roll_entry.get()
        eca_data = [
            ('Name', name_entry.get()),
            ('ECA ', eca_entry.get())
        ]  # Example fields
        save_eca_data(roll, eca_data)
        messagebox.showinfo("Success", "ECAs added successfully")
        add_eca_window.destroy()

    roll_label = tk.Label(add_eca_window, text="Roll:")
    roll_label.pack()
    roll_entry = tk.Entry(add_eca_window)
    roll_entry.pack()

    name_label = tk.Label(add_eca_window, text="NAME:")
    name_label.pack()
    name_entry = tk.Entry(add_eca_window)
    name_entry.pack()

    eca_label = tk.Label(add_eca_window, text="ECA :")
    eca_label.pack()
    eca_entry = tk.Entry(add_eca_window)
    eca_entry.pack()

    save_button = tk.Button(add_eca_window, text="Save", command=save_eca)
    save_button.pack()

    add_eca_window.mainloop()

# View ECA Window
def view_eca_window():
    # Creating Tkinter window for viewing ECA
    def delete_eca():
        selected_index = eca_list.curselection()
        if selected_index:
            selected_eca = eca_list.get(selected_index)
            roll, *ecas = selected_eca.split(" | ")
            with open(eca_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = [row for row in reader if row and row[0] != roll]
            with open(eca_database, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            messagebox.showinfo("Success", "ECA for student with roll {} deleted successfully.".format(roll))
            view_eca_window.destroy()
            view_eca_window()

    view_eca_window = tk.Tk()
    view_eca_window.title("View ECA")

    eca_list = tk.Listbox(view_eca_window, width=80, height=20)
    eca_list.pack(padx=10, pady=10)

    # Populate listbox with ECA data
    with open(eca_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            eca_list.insert(tk.END, " | ".join(row))

    delete_button = tk.Button(view_eca_window, text="Delete Selected ECA", command=delete_eca)
    delete_button.pack()

    view_eca_window.mainloop()

# Function to save student data to file
def save_student_data(data):
    with open(student_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Function to save grade data to file
def save_grade_data(roll, data):
    with open(grade_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for subject, grade in data:
            writer.writerow([roll, subject, grade])

# Function to save ECA data to file
def save_eca_data(roll, data):
    with open(eca_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for eca, name in data:
            writer.writerow([roll, eca, name])

# Starting point of the program
login_window()

# Displaying thank you message
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
