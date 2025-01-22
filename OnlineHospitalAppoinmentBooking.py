import mysql.connector
from mysql.connector import Error

# Establish the connection and create the cursor
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="Dhar2004", 
            database="besant", 
            auth_plugin="mysql_native_password"
        )
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def displaypatients():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        sql = "SELECT * FROM patients"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            pid = c[0]
            pname = c[1]
            pcell = c[2]
            print("Patient ID:", pid, "Patient Name:", pname, "Patient Cell:", pcell)
    except Error as e:
        print(f"Error fetching patients: {e}")
    finally:
        cursor.close()
        mycon.close()

def displaydoctors():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        sql = "SELECT * FROM doctors"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            did = c[0]
            dname = c[1]
            dcell = c[2]
            print("Doctor ID:", did, "Doctor Name:", dname, "Doctor Cell:", dcell)
    except Error as e:
        print(f"Error fetching doctors: {e}")
    finally:
        cursor.close()
        mycon.close()

def displayappointments():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        sql = "SELECT * FROM appointments"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            tid = c[0]
            pid = c[1]
            did = c[2]
            fees = c[3]
            Adate = c[4]
            print("Transaction ID:", tid, "Patient ID:", pid, "Doctor ID:", did, "Fees:", fees, "Appointment Date:", Adate)
    except Error as e:
        print(f"Error fetching appointments: {e}")
    finally:
        cursor.close()
        mycon.close()

def addpatient():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        pid = int(input("Enter Patient ID: "))
        pname = input("Enter Patient Name: ")
        pcell = input("Enter Patient Cell Number: ")
        sql = "INSERT INTO patients(pid, pname, pcell) VALUES (%s, %s, %s)"
        cursor.execute(sql, (pid, pname, pcell))
        mycon.commit()
        print("Patient added successfully!")
    except Error as e:
        print(f"Error adding patient: {e}")
    except ValueError:
        print("Invalid input! Please enter the correct data type.")
    finally:
        cursor.close()
        mycon.close()

def adddoctor():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        did = int(input("Enter Doctor ID: "))
        dname = input("Enter Doctor Name: ")
        dcell = input("Enter Doctor Cell Number: ")
        sql = "INSERT INTO doctors(did, dname, dcell) VALUES (%s, %s, %s)"
        cursor.execute(sql, (did, dname, dcell))
        mycon.commit()
        print("Doctor added successfully!")
    except Error as e:
        print(f"Error adding doctor: {e}")
    except ValueError:
        print("Invalid input! Please enter the correct data type.")
    finally:
        cursor.close()
        mycon.close()

def appointments():
    mycon = get_connection()
    if mycon is None:
        return
    cursor = mycon.cursor()
    try:
        print("Previous Appointments....")
        displayappointments()
        tid = int(input("Enter New Transaction ID: "))
        pid = int(input("Enter Patient ID: "))
        did = int(input("Enter Doctor ID: "))
        fees = float(input("Enter Fees: "))
        Adate = input("Enter Appointment Date (YYYY-MM-DD): ")
        sql = "INSERT INTO appointments(tid, pid, did, fees, Adate) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (tid, pid, did, fees, Adate))
        mycon.commit()
        print("Appointment added successfully!")
    except Error as e:
        print(f"Error adding appointment: {e}")
    except ValueError:
        print("Invalid input! Please enter the correct data type.")
    finally:
        cursor.close()
        mycon.close()

def main():
    choice = 'Y'
    while choice not in ['n', 'N']:
        print('WELCOME TO HOSPITAL MANAGEMENT SYSTEM\n')
        print('1. DISPLAY ALL PATIENTS DETAILS')
        print('2. DISPLAY ALL DOCTORS DETAILS')
        print('3. DISPLAY ALL APPOINTMENT DETAILS')
        print('4. ADD PATIENT DETAILS')
        print('5. ADD DOCTOR DETAILS')
        print('6. APPOINTMENT DETAILS')
        
        try:
            c = int(input("Enter your choice (1-6): "))
            if c == 1:
                displaypatients()
            elif c == 2:
                displaydoctors()
            elif c == 3:
                displayappointments()
            elif c == 4:
                addpatient()
            elif c == 5:
                adddoctor()
            elif c == 6:
                appointments()
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 6.")
        
        choice = input("Do you want to continue... Y/N: ")

if __name__ == "__main__":
    main()
