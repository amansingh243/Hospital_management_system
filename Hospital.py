
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        


        # Title Label
        self.Nameoftablet=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.numberoftablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sidefact=StringVar()
        self.furtherinformation=StringVar()
        self.storageadvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        self.Labeltitle = Label(
            self.root, 
            bd=20, 
            relief=RIDGE, 
            text="Hospital Management System", 
            fg="red", 
            bg="white", 
            font=("times new roman", 50, "bold")
        )
        self.Labeltitle.pack(fill=X)

        # ========== DATAFRAME (Parent) ==========
        Dataframe = Frame(self.root, bd=10, relief=RIDGE, padx=10, pady=10)
        Dataframe.place(x=10, y=120, width=1500, height=500)  # Adjusted size

        # ========== LEFT DATAFRAME (Inside Parent) ==========
        DataframeLeft = LabelFrame(
            Dataframe, 
            bd=10, 
            relief=RIDGE, 
            padx=10, 
            font=("arial", 12, "bold"), 
            text="Patient Information"
        )
        DataframeLeft.place(x=10, y=5, width=980, height=350)

        DataframeRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=("times new roman", 12, "bold"),text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        #==========Buttons Frame============
        Buttonframe=Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        #==========Details Frame============
        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        #===========Dataframe Left============
        lblNameTablet=Label(DataframeLeft, text="Names of Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet=ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablet, state="readonly",  
                                  font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Activan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref=Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose=Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets=Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.numberoftablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lbllot=Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lbllot.grid(row=4, column=0, sticky=W)
        txtlot=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.lot, width=35)
        txtlot.grid(row=4, column=1)

        lblIssueDate=Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.issuedate, width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate=Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.expdate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose=Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.dailydose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect=Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.sidefact, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinformation=Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherinformation.grid(row=0, column=2, sticky=W)
        txtFurtherinformation=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.furtherinformation, width=35)
        txtFurtherinformation.grid(row=0, column=3)

        lblBloodPressure=Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage=Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.storageadvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine=Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber=Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6, column=3)

        lblDateOfBirth=Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress=Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        #==============DataFrameRight==============
        self.txtPrescription=Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #=============Buttons=================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.prescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.delete)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.clear)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", 
                         font=("Arial", 12, "bold"), width=23, height=2,
                         command=self.exit)
        btnExit.grid(row=0, column=5)

        #==================Table=================
        #========scrollbar===============
        Scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe, columns=("nameoftablet", "ref", "dose", "nooftablets", 
                                                               "lot", "issuedate", "expdate", "dailydose", 
                                                               "storage", "nhsnumber", "pname", "dob", "address"), 
                                                               xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.hospital_table.xview)
        Scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet", text="Name of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        
        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def iPrescription(self):
        if self.Nameoftablet.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            self.txtPrescription.delete("1.0", END)
            self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablet.get() + "\n")
            self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
            self.txtPrescription.insert(END, "Dose:\t\t\t" + self.dose.get() + "\n")
            self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.numberoftablets.get() + "\n")
            self.txtPrescription.insert(END, "Lot:\t\t\t" + self.lot.get() + "\n")
            self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.issuedate.get() + "\n")
            self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.expdate.get() + "\n")
            self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.dailydose.get() + "\n")
            self.txtPrescription.insert(END, "Side Effects:\t\t\t" + self.sidefact.get() + "\n")
            self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.furtherinformation.get() + "\n")
            self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.storageadvice.get() + "\n")
            self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
            self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientId.get() + "\n")
            self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
            self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
            self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
            self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def prescriptionData(self):
        if self.Nameoftablet.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="aman24",
                    database="new_schema"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.Nameoftablet.get(),
                    self.ref.get(),
                    self.dose.get(),
                    self.numberoftablets.get(),
                    self.lot.get(),
                    self.issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.storageadvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="aman24",
            database="new_schema"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                self.hospital_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        
        self.Nameoftablet.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.numberoftablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storageadvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def update_data(self):
        if self.Nameoftablet.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="aman24",
                    database="new_schema"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE hospital SET nameoftablet=%s, dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storageadvice=%s, nhsnumber=%s, patientname=%s, DateOfBirth=%s, PatientAddress=%s WHERE ref=%s", (
                    self.Nameoftablet.get(),
                    self.dose.get(),
                    self.numberoftablets.get(),
                    self.lot.get(),
                    self.issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.storageadvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get(),
                    self.ref.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been updated")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")

    def delete(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference No. is required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="aman24",
                    database="new_schema"
                )
                my_cursor = conn.cursor()
                sql = "DELETE FROM hospital WHERE ref=%s"
                value = (self.ref.get(),)
                my_cursor.execute(sql, value)
                
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Success", "Record has been deleted")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")

    def clear(self):
        self.Nameoftablet.set("")
        self.ref.set("")
        self.dose.set("")
        self.numberoftablets.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sidefact.set("")
        self.furtherinformation.set("")
        self.storageadvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def exit(self):
        exit_confirm = messagebox.askyesno("Hospital Management System", "Do you want to exit?")
        if exit_confirm:
            root.destroy()
            return

if __name__ == "__main__":
    root = Tk()
    application = Hospital(root)
    root.mainloop()