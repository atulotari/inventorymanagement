import os
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class AdminClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================================= Variables =============================
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        self.admin_id_var = StringVar()
        self.admin_id_var.set("1")
        self.admin_gender_var = StringVar()
        self.admin_contact_var = StringVar()
        self.admin_name_var = StringVar()
        self.admin_dob_var = StringVar()
        self.admin_doj_var = StringVar()
        self.admin_email_var = StringVar()
        self.admin_password_var = StringVar()
        self.admin_user_type_var = StringVar()
        self.admin_salary_var = StringVar()

        # =================================== Title ================================
        title = Label(self.root, text="Admin Details", font=("goudy old style", 16, "bold"), bg="#0f4d7d",
                      fg="white")
        title.place(x=50, y=10, width=1000)

        welcome_note = Label(self.root, text="* You Have Authority to Access All Details in This Software *",
                             font=("goudy old style", 15, "bold"), bg="white", fg="green")
        welcome_note.place(x=50, y=50, width=1000)

        # =================================== Content ==============================
        # =================================== Row 1 ==============================
        admin_id_lbl = Label(self.root, text="Admin ID", font=("goudy old style", 15, "bold"), bg="white")
        admin_id_lbl.place(x=50, y=130)
        admin_id_txt = Entry(self.root, textvariable=self.admin_id_var, font=("goudy old style", 15, "bold"),
                             bg="light yellow")
        admin_id_txt.place(x=150, y=130, width=180)

        admin_gender_lbl = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white")
        admin_gender_lbl.place(x=350, y=130)
        admin_gender_cmb = ttk.Combobox(self.root, values=("Select", "Male", "Female", "Other"), state="readonly",
                                        justify=CENTER, font=("goudy old style", 15),
                                        textvariable=self.admin_gender_var)
        admin_gender_cmb.place(x=500, y=130, width=180)
        admin_gender_cmb.current(0)

        admin_contact_lbl = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white")
        admin_contact_lbl.place(x=750, y=130)
        admin_contact_txt = Entry(self.root, textvariable=self.admin_contact_var, font=("goudy old style", 15, "bold"),
                                  bg="light yellow")
        admin_contact_txt.place(x=850, y=130, width=180)

        # =================================== Row 2 ==============================
        admin_name_lbl = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white")
        admin_name_lbl.place(x=50, y=200)
        admin_name_txt = Entry(self.root, textvariable=self.admin_name_var, font=("goudy old style", 15, "bold"),
                               bg="light yellow")
        admin_name_txt.place(x=150, y=200, width=180)

        admin_dob_lbl = Label(self.root, text="D.O.B.", font=("goudy old style", 15, "bold"), bg="white")
        admin_dob_lbl.place(x=350, y=200)
        admin_dob_txt = Entry(self.root, textvariable=self.admin_dob_var, font=("goudy old style", 15, "bold"),
                              bg="light yellow")
        admin_dob_txt.place(x=500, y=200, width=180)

        admin_doj_lbl = Label(self.root, text="D.O.J.", font=("goudy old style", 15, "bold"), bg="white")
        admin_doj_lbl.place(x=750, y=200)
        admin_doj_txt = Entry(self.root, textvariable=self.admin_doj_var, font=("goudy old style", 15, "bold"),
                              bg="light yellow")
        admin_doj_txt.place(x=850, y=200, width=180)

        # =================================== Row 3 ==============================
        admin_email_lbl = Label(self.root, text="E-mail", font=("goudy old style", 15, "bold"), bg="white")
        admin_email_lbl.place(x=50, y=270)
        admin_email_txt = Entry(self.root, textvariable=self.admin_email_var, font=("goudy old style", 15, "bold"),
                                bg="light yellow")
        admin_email_txt.place(x=150, y=270, width=180)

        admin_password_lbl = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), bg="white")
        admin_password_lbl.place(x=350, y=270)
        admin_password_txt = Entry(self.root, textvariable=self.admin_password_var,
                                   font=("goudy old style", 15, "bold"), bg="light yellow")
        admin_password_txt.place(x=500, y=270, width=180)

        admin_user_type_lbl = Label(self.root, text="User Type", font=("goudy old style", 15, "bold"), bg="white")
        admin_user_type_lbl.place(x=750, y=270)
        admin_user_type_cmb = ttk.Combobox(self.root, values="Admin", state="readonly",
                                           justify=CENTER, font=("goudy old style", 15),
                                           textvariable=self.admin_user_type_var)
        admin_user_type_cmb.place(x=850, y=270, width=180)
        admin_user_type_cmb.current(0)

        # =================================== Row 4 ==============================
        admin_address_lbl = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white")
        admin_address_lbl.place(x=50, y=340)
        self.admin_address_txt = Text(self.root, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.admin_address_txt.place(x=150, y=340, width=300, height=60)

        admin_salary_lbl = Label(self.root, text="Salary", font=("goudy old style", 15, "bold"), bg="white")
        admin_salary_lbl.place(x=500, y=340)
        admin_salary_txt = Entry(self.root, textvariable=self.admin_salary_var,
                                 font=("goudy old style", 15, "bold"), bg="light yellow", state="readonly")
        admin_salary_txt.place(x=600, y=340, width=180)
        self.admin_salary_var.set("N/A")

        # =================================== Buttons =============================
        add_btn = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white",
                         cursor="hand2", command=self.add)
        add_btn.place(x=500, y=375, width=130, height=28)

        clear_btn = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear)
        clear_btn.place(x=650, y=375, width=130, height=28)

        note_lbl = Label(self.root, text="Note: Please Enter Valid 'E-Mail ID', To Make Easy To Reset Your Password When You Forget !",
                         font=("goudy old style", 15, "bold"), bg="white", fg="red", pady=30)
        note_lbl.pack(side=BOTTOM, fill=X)

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.admin_id_var.get() == "":
                messagebox.showerror("Error", "Admin ID Must Be Required !", parent=self.root)

            elif self.admin_id_var.get() != "1":
                messagebox.showerror("Error", "Admin ID Must Be '1', \nTheir Has to be Only 1 Admin User !", parent=self.root)
                self.admin_id_var.set("1")

            elif self.admin_name_var.get() == "" or self.admin_email_var.get() == "" or self.admin_gender_var.get() == "" or self.admin_contact_var.get() == "" or self.admin_dob_var.get() == "" or self.admin_doj_var.get() == "" or self.admin_password_var.get() == "" or self.admin_user_type_var.get() == "" or self.admin_address_txt.get(
                    '1.0', END) == "" or self.admin_salary_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from employee where e_id=?", (self.admin_id_var.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID is Already Present, Try Different One.",
                                         parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee (e_id, name, email, gender, contact, dob, doj, pass, u_type, address, salary) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.admin_id_var.get(),
                            self.admin_name_var.get(),
                            self.admin_email_var.get(),
                            self.admin_gender_var.get(),
                            self.admin_contact_var.get(),
                            self.admin_dob_var.get(),
                            self.admin_doj_var.get(),
                            self.admin_password_var.get(),
                            self.admin_user_type_var.get(),
                            self.admin_address_txt.get('1.0', END),
                            self.admin_salary_var.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Admin Added Successfully.", parent=self.root)
                    messagebox.showinfo("Success", "Now, You Have to Login as Admin From Login Page With Given Details !", parent=self.root)
                    self.root.destroy()
                    os.system("python Login.py")
                con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.admin_id_var.set("1")
        self.admin_name_var.set("")
        self.admin_email_var.set("")
        self.admin_gender_var.set("Select")
        self.admin_contact_var.set("")
        self.admin_dob_var.set("")
        self.admin_doj_var.set("")
        self.admin_password_var.set("")
        self.admin_user_type_var.set("Admin")
        self.admin_address_txt.delete('1.0', END)
        self.admin_salary_var.set("")


if __name__ == '__main__':
    root = Tk()
    obj = AdminClass(root)
    root.mainloop()
