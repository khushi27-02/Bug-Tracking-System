import sqlite3 as sql

# Create or connect to the SQLite database
con = sql.connect("bug_tracking_system.db")
cursor = con.cursor()
# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        empCode INT PRIMARY KEY,
        empName VARCHAR(30),
        empEmail VARCHAR(40),
        empPassword VARCHAR(20),
        gender VARCHAR(10),
        DOB VARCHAR(20),
        mobileNo BIG INT,
        Role VARCHAR(20)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS AssignProject (
        projectID INT FK,
        empCode INT FK
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Project (
        projectID INT PRIMARY KEY,
        projectName VARCHAR(30),
        SDate VARCHAR(30),
        EDate VARCHAR(30),
        projectDec VARCHAR(200)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS BugReport (
        bugNo INT PRIMARY KEY,
        bugCode INT FK,
        projectID INT FK,
        TCode INT FK,
        ECode INT FK,
        status VARCHAR(20),
        bugDes VARCHAR(100)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS BugType (
        bugCode INT PRIMARY KEY,
        bugCategory VARCHAR(30),
        bugSeverity VARCHAR(20)
    )
''')

# Manager Functions
def add_manager(empName, empEmail, empPassword, gender, DOB, mobileNo):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO Employee (empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (empName, empEmail, empPassword, gender, DOB, mobileNo, "Manager"))
    con.commit()
    con.close()

def view_managers():
    con = sql.connect('bug_tracking_system.db') 
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Employee WHERE Role = "Manager"')
    managers = cursor.fetchall()
    con.close()
    return managers

def delete_manager(empCode):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM Employee WHERE empCode = ? AND Role = "Manager"', (empCode,))
    con.commit()
    con.close()

def update_manager(empCode, new_email, new_mobile):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE Employee
        SET empEmail = ?, mobileNo = ?
        WHERE empCode = ? AND Role = "Manager"
    ''', (new_email, new_mobile, empCode))
    con.commit()
    con.close()

# Employee Functions
def add_employee(empName, empEmail, empPassword, gender, DOB, mobileNo, Role):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO Employee (empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
    con.commit()
    con.close()

def view_employees():
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Employee')
    employees = cursor.fetchall()
    con.close()
    return employees

def delete_employee(empCode):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM Employee WHERE empCode = ?', (empCode,))
    con.commit()
    con.close()

def update_employee(empCode, new_email, new_mobile):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE Employee
        SET empEmail = ?, mobileNo = ?
        WHERE empCode = ?
    ''', (new_email, new_mobile, empCode))
    con.commit()
    con.close()

# Functions for viewing projects and bug reports
def view_all_projects():
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Project')
    projects = cursor.fetchall()
    con.close()
    return projects

def view_all_bug_reports():
    con = sql.connect('bug_tracking_system.db') 
    cursor = con.cursor()
    cursor.execute('SELECT * FROM BugReport')
    bug_reports = cursor.fetchall()
    con.close()
    return bug_reports

# In the main loop of the Admin Module:
if __name__ == "__main__":
    print("Admin Module")

    while True:
        print("\nOptions:")
        print("1. Manager")
        print("2. Employee")
        print("3. View All Project")
        print("4. View Bug's Reports")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nManager:")
            print("1. Add Manager Account")
            print("2. View Manager Account")
            print("3. Delete Manager")
            print("4. Update Manager Details")

            manager_choice = int(input("Enter your choice: "))

            if manager_choice == 1:
                empName = input("Enter manager's name: ")
                empEmail = input("Enter manager's email: ")
                empPassword = input("Enter manager's password: ")
                gender = input("Enter manager's gender: ")
                DOB = input("Enter manager's date of birth: ")
                mobileNo = int(input("Enter manager's mobile number: "))
                add_manager(empName, empEmail, empPassword, gender, DOB, mobileNo)
                print("Manager account added successfully!")

            elif manager_choice == 2:
                managers = view_managers()
                for manager in managers:
                    print(manager)

            elif manager_choice == 3:
                empCode = int(input("Enter empCode of the manager to delete: "))
                delete_manager(empCode)
                print("Manager account deleted successfully!")

            elif manager_choice == 4:
                empCode = int(input("Enter empCode of the manager to update: "))
                new_email = input("Enter new email: ")
                new_mobile = int(input("Enter new mobile number: "))
                update_manager(empCode, new_email, new_mobile)
                print("Manager account updated successfully!")

            else:
                print("Invalid choice for managing managers.")

        elif choice == 2:
            print("\nEmployee:")
            print("1. Add Employee Account")
            print("2. View Employee's Account")
            print("3. Delete Employee Account")
            print("4. Update Employee Details")

            employee_choice = int(input("Enter your choice: "))

            if employee_choice == 1:
                empName = input("Enter employee's name: ")
                empEmail = input("Enter employee's email: ")
                empPassword = input("Enter employee's password: ")
                gender = input("Enter employee's gender: ")
                DOB = input("Enter employee's date of birth: ")
                mobileNo = int(input("Enter employee's mobile number: "))
                Role = input("Enter employee's role: ")
                add_employee(empName, empEmail, empPassword, gender, DOB, mobileNo, Role)
                print("Employee account added successfully!")

            elif employee_choice == 2:
                employees = view_employees()
                for employee in employees:
                    print(employee)

            elif employee_choice == 3:
                empCode = int(input("Enter empCode of the employee to delete: "))
                delete_employee(empCode)
                print("Employee account deleted successfully!")

            elif employee_choice == 4:
                empCode = int(input("Enter empCode of the employee to update: "))
                new_email = input("Enter new email: ")
                new_mobile = int(input("Enter new mobile number: "))
                update_employee(empCode, new_email, new_mobile)
                print("Employee account updated successfully!")

            else:
                print("Invalid choice for managing employees.")

        elif choice == 3:
            projects = view_all_projects()
            for project in projects:
                print(project)

        elif choice == 4:
            bug_reports = view_all_bug_reports()
            for bug_report in bug_reports:
                print(bug_report)         

        elif choice == 5:
            print("Exiting the Admin Module...")
            break

        else:
            print("Invalid choice. Please choose again.")

