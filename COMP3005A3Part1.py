import psycopg

def connectDatabase():
    try:
        connect = psycopg.connect(
            dbname = "postgres",
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = "5432"
        )
        return connect
    except:
        print("Not able to connect")


def getAllStudents():
    connect = connectDatabase()
    try:
        cur = connect.cursor()
        cur.execute("SELECT * FROM students")
        res = cur.fetchall()
        for s in res:
            print(s)
    except:
        print("\nError! Connection Failed!")
    finally:
        cur.close();

def addStudent(first_name, last_name, email, enrollment_date):
    connect = connectDatabase()
    try:
        cur = connect.cursor()
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        connect.commit()
        print("\nAdded Student!")
    except:
        print("\nFailed to add student!")
    finally:
        cur.close()

def updateStudentEmail (student_id, new_email):
    connect = connectDatabase()
    try:
        cur = connect.cursor()
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        connect.commit()
        print("\nEmail Updated!")
    except:
        print("\nFailed to update email!")
    finally:
        cur.close()

def deleteStudent(student_id):
    connect = connectDatabase()
    try:
        cur = connect.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connect.commit()
        print("\nStudent Deleted!")
    except:
        print("\nFailed to delete student!")
    finally:
        cur.close()

def main():
    choice = ''
    while(1):
        print("\n1. Show all students.")
        print("2. Add a new student.")
        print("3. Update email for a student.")
        print("4. Delete a student.")
        
        choice = input("\nEnter the number corresponding to the action: ")

        if(choice == 'q' or choice == 'Q'):
            print("Quiting")
            break

        elif(choice == "1"):
            print("\n")
            getAllStudents()
        
        elif (choice == "2"):
            fName = input("\nEnter the student's first name: ")
            lName = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            date = input("Enter the student's enrollment date in the following format YYYY-MM-DD: ")
            addStudent(fName, lName, email, date)
        
        elif (choice == "3"):
            id = input ("\nEnter the student's id: ")
            nEmail = input ("Enter the student's new email: ")
            updateStudentEmail(id, nEmail)

        elif (choice == "4"):
            id = input ("\nEnter the student's id: ")
            deleteStudent(id)

        else:
            print("\nEnter a valid choice or q to quit")

main()
