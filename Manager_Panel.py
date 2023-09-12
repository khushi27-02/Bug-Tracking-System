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

# Function to update the manager's profile
def update_profile(empCode, new_email, new_mobile):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE Employee
        SET empEmail = ?, mobileNo = ?
        WHERE empCode = ?
    ''', (new_email, new_mobile, empCode))
    con.commit()
    con.close()

# Function to add a project
def add_project(projectName, SDate, EDate, projectDec):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO Project (projectName, SDate, EDate, projectDec)
        VALUES (?, ?, ?, ?)
    ''', (projectName, SDate, EDate, projectDec))
    con.commit()
    con.close()

# Function to view all projects
def view_projects():
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Project')
    projects = cursor.fetchall()
    con.close()
    return projects

# Function to delete a project
def delete_project(projectID):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM Project WHERE projectID = ?', (projectID,))
    con.commit()
    con.close()

# Function to update a project
def update_project(projectID, projectName, SDate, EDate, projectDec):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE Project
        SET projectName = ?, SDate = ?, EDate = ?, projectDec = ?
        WHERE projectID = ?
    ''', (projectName, SDate, EDate, projectDec, projectID))
    con.commit()
    con.close()
    
# Functions of bugs
def add_bug(bugCode, projectID, TCode, ECode, bugDes):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO BugReport (bugCode, projectID, TCode, ECode, status, bugDes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (bugCode, projectID, TCode, ECode, 'pending', bugDes))
    con.commit()
    con.close()

def view_all_bugs():
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM BugReport')
    bugs = cursor.fetchall()
    con.close()
    return bugs

def update_bug(bugNo, new_status):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE BugReport
        SET status = ?
        WHERE bugNo = ?
    ''', (new_status, bugNo))
    con.commit()
    con.close()

def delete_bug(bugNo):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM BugReport WHERE bugNo = ?', (bugNo,))
    con.commit()
    con.close()

def view_bug_details(bugNo):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM BugReport WHERE bugNo = ?', (bugNo,))
    bug = cursor.fetchone()
    con.close()
    return bug

# In the main loop of the Manager Panel:
if __name__ == "__main__":
    print("Manager Panel")
    empCode = int(input("Enter your empCode: "))

    while True:
        print("\nOptions:")
        print("1. Update Profile")
        print("2. Manage Project")
        print("3. Bug's")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_email = input("Enter new email: ")
            new_mobile = int(input("Enter new mobile number: "))
            update_profile(empCode, new_email, new_mobile)
            print("Profile updated successfully!")

        elif choice == 2:
            print("\nManage Project:")
            print("1. Add Project")
            print("2. View All Projects")
            print("3. Delete Project")
            print("4. Update Project")

            project_choice = int(input("Enter your choice: "))

            if project_choice == 1:
                projectName = input("Enter project name: ")
                SDate = input("Enter start date: ")
                EDate = input("Enter end date: ")
                projectDec = input("Enter project description: ")
                add_project(projectName, SDate, EDate, projectDec)
                print("Project added successfully!")

            elif project_choice == 2:
                projects = view_projects()
                for project in projects:
                    print(project)

            elif project_choice == 3:
                projectID = int(input("Enter project ID to delete: "))
                delete_project(projectID)
                print("Project deleted successfully!")

            elif project_choice == 4:
                projectID = int(input("Enter project ID to update: "))
                projectName = input("Enter new project name: ")
                SDate = input("Enter new start date: ")
                EDate = input("Enter new end date: ")
                projectDec = input("Enter new project description: ")
                update_project(projectID, projectName, SDate, EDate, projectDec)
                print("Project updated successfully!")

            else:
                print("Invalid choice for managing projects.")

        elif choice == 3:
            print("\nBug's:")
            print("1. Add New Bug")
            print("2. View All Bug’s")
            print("3. Update Bug")
            print("4. Delete Bug")

            bug_choice = int(input("Enter your choice: "))

            if bug_choice == 1:
                bugCode = int(input("Enter bug code: "))
                projectID = int(input("Enter project ID: "))
                TCode = empCode
                ECode = empCode
                bugDes = input("Enter bug description: ")
                add_bug(bugCode, projectID, TCode, ECode, bugDes)
                print("Bug added successfully!")

            elif bug_choice == 2:
                bugs = view_all_bugs()
                for bug in bugs:
                    print(bug)

            elif bug_choice == 3:
                bugNo = int(input("Enter bug number to update: "))
                new_status = input("Enter new status (pending/resolved): ")
                update_bug(bugNo, new_status)
                print("Bug status updated successfully!")

            elif bug_choice == 4:
                bugNo = int(input("Enter bug number to delete: "))
                delete_bug(bugNo)
                print("Bug deleted successfully!")

            else:
                print("Invalid choice for managing bugs.")

        elif choice == 4:
            print("Exiting the Manager Panel...")
            break

        else:
            print("Invalid choice. Please choose again.")
