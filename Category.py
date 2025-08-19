import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class CategoryClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========================================= Variables =======================================
        self.cat_id_var = StringVar()
        self.cat_name_var = StringVar()

        # ========================================= Title =======================================
        title_lbl = Label(self.root, text="Manage Product Category", font=("goudy old style", 30, "bold"), bg="#184a45",
                          fg="white", bd=3, relief=RIDGE)
        title_lbl.pack(side=TOP, fill=X, padx=10, pady=20)

        name_lbl = Label(self.root, text="Enter Category Name", font=("goudy old style", 30, "bold"), bg="white")
        name_lbl.place(x=50, y=100)

        name_txt = Entry(self.root, textvariable=self.cat_name_var, font=("goudy old style", 18), bg="light yellow")
        name_txt.place(x=50, y=170, width=300)

        add_btn = Button(self.root, text="Add", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white",
                         cursor="hand2", command=self.add)
        add_btn.place(x=360, y=169, width=150, height=32)

        delete_btn = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="red", fg="white",
                            cursor="hand2", command=self.delete)
        delete_btn.place(x=520, y=169, width=150, height=32)

        # ================================= Category Details ==============================
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=100)

        scroll_x = Scrollbar(cat_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(cat_frame, orient=VERTICAL)

        self.category_table = ttk.Treeview(cat_frame, columns=("c_id", "name"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.category_table.xview)
        scroll_y.config(command=self.category_table.yview)

        self.category_table.heading("c_id", text="C ID")
        self.category_table.heading("name", text="Name")
        self.category_table["show"] = "headings"

        self.category_table.column("c_id", width=90)
        self.category_table.column("name", width=100)
        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)

        # ================================= Images ==============================
        self.img_1 = Image.open("Images\\cat.jpg")
        self.img_1 = self.img_1.resize((500, 250))
        self.img_1 = ImageTk.PhotoImage(self.img_1)

        self.img_1_lbl = Label(self.root, image=self.img_1, bd=2, relief=RAISED)
        self.img_1_lbl.place(x=50, y=220)

        self.img_2 = Image.open("Images\\category.jpg")
        self.img_2 = self.img_2.resize((500, 250))
        self.img_2 = ImageTk.PhotoImage(self.img_2)

        self.img_2_lbl = Label(self.root, image=self.img_2, bd=2, relief=RAISED)
        self.img_2_lbl.place(x=580, y=220)

        self.show()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.cat_name_var.get() == "":
                messagebox.showerror("Error", "Category Name Must Be Required !", parent=self.root)

            else:
                cur.execute("select * from category where name=?", (self.cat_name_var.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category is Already Present, Try Different One.",
                                         parent=self.root)
                else:
                    cur.execute("insert into category (name) values(?)", (self.cat_name_var.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully.", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row = content['values']
        self.cat_id_var.set(row[0])
        self.cat_name_var.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.cat_id_var.get() == "":
                messagebox.showerror("Error", "Please Select Category From The List!", parent=self.root)

            elif self.cat_name_var.get() == "":
                messagebox.showerror("Error", "All Fields Are Required !", parent=self.root)

            else:
                cur.execute("select * from category where c_id=?", (self.cat_id_var.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Error, Please Try Again !", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Do You Really Want to Delete ?", parent=self.root)
                    if option is True:
                        cur.execute("delete from category where c_id=?", (self.cat_id_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.cat_id_var.set("")
                        self.cat_name_var.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()
