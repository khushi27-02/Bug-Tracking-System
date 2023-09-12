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

# Function to update the employee's profile
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

# Function to add a bug report
def add_bug_report(empCode, bugCode, projectID, TCode, ECode, bugDes):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO BugReport (bugCode, projectID, TCode, ECode, status, bugDes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (bugCode, projectID, TCode, ECode, 'pending', bugDes))
    con.commit()
    con.close()

# Function to update bug status
def update_bug_status(bugNo, new_status):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('''
        UPDATE BugReport
        SET status = ?
        WHERE bugNo = ?
    ''', (new_status, bugNo))
    con.commit()
    con.close()

# Function to view all bugs
def view_bugs():
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM BugReport')
    bugs = cursor.fetchall()
    con.close()
    return bugs

# Function to view bug details
def bug_details(bugNo):
    con = sql.connect('bug_tracking_system.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM BugReport WHERE bugNo = ?', (bugNo,))
    bug = cursor.fetchone()
    con.close()
    return bug

if __name__ == "__main__":
    print("Employee Panel")
    empCode = int(input("Enter your empCode: "))

    while True:
        print("\nOptions:")
        print("1. Update Profile")
        print("2. Add Bug's Report")
        print("3. Update Bug status")
        print("4. View Bug's")
        print("5. Bug Detail’s")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_email = input("Enter new email: ")
            new_mobile = int(input("Enter new mobile number: "))
            update_profile(empCode, new_email, new_mobile)
            print("Profile updated successfully!")

        elif choice == 2:
            bugCode = int(input("Enter bug code: "))
            projectID = int(input("Enter project ID: "))
            TCode = empCode
            ECode = empCode
            bugDes = input("Enter bug description: ")
            add_bug_report(empCode, bugCode, projectID, TCode, ECode, bugDes)
            print("Bug report added successfully!")

        elif choice == 3:
            bugNo = int(input("Enter bug number: "))
            new_status = input("Enter new status (pending/resolved): ")
            update_bug_status(bugNo, new_status)
            print("Bug status updated successfully!")

        elif choice == 4:
            bugs = view_bugs()
            for bug in bugs:
                print(bug)

        elif choice == 5:
            bugNo = int(input("Enter bug number: "))
            bug = bug_details(bugNo)
            print(bug)

        elif choice == 6:
            print("Exiting the Employee Panel...")
            break

        else:
            print("Invalid choice. Please choose again.")

