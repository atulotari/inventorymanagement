import os
import time
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk
import Email_pass
import smtplib


class LoginSystem:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # ============================= Variables ===========================
        self.employee_id = StringVar()
        self.password_var = StringVar()
        self.otp = ''

        # =============================== Images ============================
        self.phone_image = ImageTk.PhotoImage(file="Images\\phone.png")
        self.phone_img_lbl = Label(self.root, image=self.phone_image, bd=0)
        self.phone_img_lbl.place(x=200, y=50)

        # ============================= Login Frame =========================
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title_lbl = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg="white")
        title_lbl.place(x=0, y=30, relwidth=1)

        employee_id_lbl = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171")
        employee_id_lbl.place(x=50, y=120)
        user_txt = Entry(login_frame, font=("times new roman", 15), bg="light yellow", textvariable=self.employee_id)
        user_txt.place(x=50, y=160, width=250)

        password_lbl = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
        password_lbl.place(x=50, y=200)
        password_txt = Entry(login_frame, font=("times new roman", 15), bg="light yellow", textvariable=self.password_var, show="*")
        password_txt.place(x=50, y=240, width=250)

        login_btn = Button(login_frame, text="Sign In", font=("Arial Rounded MT Bold", 15), bg="#00B0F0", cursor="hand2",
                           activebackground="#00B0F0", fg="black", activeforeground="white", command=self.admin_sign_in)
        login_btn.place(x=100, y=300, width=150, height=35)

        self.login_btn = Button(login_frame, text="Log In", font=("Arial Rounded MT Bold", 15), bg="#00B0F0", cursor="hand2",
                                activebackground="#00B0F0", fg="black", activeforeground="white", command=self.login)
        self.login_btn.place(x=100, y=300, width=150, height=35)

        horizontal_row_lbl = Label(login_frame, bg="light gray")
        horizontal_row_lbl.place(x=50, y=370, width=250, height=2)
        or_lbl = Label(login_frame, text="OR", font=("times new roman", 15, "bold"), bg="white", fg="light gray")
        or_lbl.place(x=150, y=356)

        forget_pass = Button(login_frame, text="Forget Password ?", font=("times new roman", 13, "bold"), bg="white", fg="#00759E",
                             bd=0, cursor="hand2", activebackground="white", activeforeground="#00759E", command=self.forget_window)
        forget_pass.place(x=100, y=400)

        # ============================================= Frame 2 ==========================================
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        register_lbl = Label(register_frame, text="Developed By Yuva Net Cafe", font=("times new roman", 13), bg="white")
        register_lbl.place(x=0, y=15, relwidth=1)

        # ============================================ Animation img =============================================
        self.image_1 = ImageTk.PhotoImage(file="Images\\im1.png")
        self.image_2 = ImageTk.PhotoImage(file="Images\\im2.png")
        self.image_3 = ImageTk.PhotoImage(file="Images\\im3.png")

        self.change_image_lbl = Label(self.root, bg="white")
        self.change_image_lbl.place(x=367, y=153, width=240, height=428)

        self.animate()
        self.chk_user_type()

    def animate(self):
        img = self.image_1
        self.image_1 = self.image_2
        self.image_2 = self.image_3
        self.image_3 = img
        self.change_image_lbl.config(image=img)
        self.change_image_lbl.after(2000, self.animate)

    def chk_user_type(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            user = cur.fetchall()
            if len(user) == 0:
                messagebox.showerror("Error", "No Admin or Employee is Present, Kindly Sign In as a Admin.")
                self.login_btn.destroy()
            else:
                pass

        except Exception as error:
            messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def login(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            else:
                cur.execute("select u_type from employee where e_id=? AND pass=?", (
                    self.employee_id.get(), self.password_var.get()
                ))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    if user == "Admin":
                        self.root.destroy()
                        os.system("python Dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python Billing.py")

        except Exception as error:
            messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def admin_sign_in(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            user = cur.fetchall()
            if len(user) == 0:
                self.root.destroy()
                os.system("python Admin_pass_recover.py")
            else:
                if self.employee_id.get() == "" or self.password_var.get() == "":
                    messagebox.showerror("Error", "All Fields Must Be Empty !", parent=self.root)
                else:

                    cur.execute("select u_type from employee where e_id=? AND pass=?", (
                        self.employee_id.get(), self.password_var.get()
                    ))
                    users = cur.fetchone()[0]

                    if users is None:
                        messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                    else:
                        if str(users) == "Admin":
                            self.root.destroy()
                            os.system("python Dashboard.py")
                        else:
                            self.root.destroy()
                            os.system("python Billing.py")

        except Exception as error:
            messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def forget_window(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required !", parent=self.root)
            else:
                cur.execute("select email from employee where e_id=?", (self.employee_id.get(),))
                email = cur.fetchone()[0]
                if email is None:
                    messagebox.showerror("Error", "Invalid Employee ID, Try Again !", parent=self.root)
                else:
                    self.otp_var = StringVar()
                    self.new_pass_var = StringVar()
                    self.conf_pass_var = StringVar()
                    check = self.send_email(email)
                    if check == "Failed":
                        messagebox.showerror("Error", "Connection Error, try again", parent=self.root)
                    else:
                        # ====================================== Forget Window =====================================
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title("Reset Password")
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()

                        # ========================================== Title =========================================
                        title = Label(self.forget_win, text="Reset Password", font=("goudy old style", 15, "bold"),
                                      bg="#3f51b5", fg="white")
                        title.pack(side=TOP, fill=X)

                        reset_lbl = Label(self.forget_win, text="Enter OTP Send on Registered E-mail", font=("times new roman", 15))
                        reset_lbl.place(x=20, y=60)
                        reset_txt = Entry(self.forget_win, textvariable=self.otp_var, font=("times new roman", 15), bg="light yellow")
                        reset_txt.place(x=20, y=100, width=250, height=30)

                        self.reset_btn = Button(self.forget_win, text="Submit", font=("times new roman", 15, "bold"), bg="light blue", cursor="hand2", command=self.validate_otp)
                        self.reset_btn.place(x=280, y=100, width=100, height=30)

                        new_pass_lbl = Label(self.forget_win, text="New Password", font=("times new roman", 15))
                        new_pass_lbl.place(x=20, y=160)
                        new_pass_txt = Entry(self.forget_win, textvariable=self.new_pass_var, font=("times new roman", 15), bg="light yellow")
                        new_pass_txt.place(x=20, y=190, width=250, height=30)

                        conf_pass_lbl = Label(self.forget_win, text="Confirm Password", font=("times new roman", 15))
                        conf_pass_lbl.place(x=20, y=225)
                        conf_pass_txt = Entry(self.forget_win, textvariable=self.conf_pass_var, font=("times new roman", 15), bg="light yellow")
                        conf_pass_txt.place(x=20, y=250, width=250, height=30)

                        self.update_btn = Button(self.forget_win, text="Update", font=("times new roman", 15, "bold"), bg="light blue", cursor="hand2", state=DISABLED, command=self.update_password)
                        self.update_btn.place(x=150, y=300, width=100, height=30)

        except Exception as error:
            messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def send_email(self, to):
        sm = smtplib.SMTP('smtp.gmail.com', 587)
        sm.starttls()
        e_mail = Email_pass.developer_email
        pass_word = Email_pass.pass_for_mail
        sm.login(e_mail, pass_word)
        self.otp = int(time.strftime("%H%S%M")) + int(time.strftime("%S"))
        subj = "IMS-Reset Password OTP"
        msg = f"Dear Sir/Madam, \n\n\tYour OTP for resetting password is {str(self.otp)}.\n\nWith Regards,\nIMS Developer - Atul Otari."
        msg = "Subject:{}\n\n{}".format(subj, msg)
        sm.sendmail(e_mail, to, msg)
        check = sm.ehlo()
        if check[0] == 250:
            return 'Success'
        else:
            return 'Failed'

    def update_password(self):
        if self.new_pass_var.get() == "" or self.conf_pass_var.get() == "":
            messagebox.showerror("Error", "Password is Required !", parent=self.forget_win)
        elif self.new_pass_var.get() != self.conf_pass_var.get():
            messagebox.showerror("Error", "New Password & Confirm Password Must be Same !", parent=self.forget_win)
        else:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            try:
                cur.execute("update employee set pass=? where e_id=?", (self.new_pass_var.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success", "Password Updated Successfully", parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as error:
                messagebox.showerror("Error", f"Error Due To : {str(error)}", parent=self.root)

    def validate_otp(self):
        if int(self.otp) == int(self.otp_var.get()):
            self.update_btn.config(state=NORMAL)
            self.reset_btn.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTP, Try Again !", parent=self.forget_win)


root = Tk()
obj = LoginSystem(root)
root.mainloop()
