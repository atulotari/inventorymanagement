from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk, messagebox


class SalesClass:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry("1100x500+225+150")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ====================================== Variables ======================================
        self.invoice_var = StringVar()
        self.bill_list = []

        # ========================================= Title =======================================
        title_lbl = Label(self.root, text="View Customer Bills", font=("goudy old style", 30, "bold"), bg="#184a45",
                          fg="white", bd=3, relief=RIDGE)
        title_lbl.pack(side=TOP, fill=X, padx=10, pady=20)

        invoice_lbl = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white")
        invoice_lbl.place(x=50, y=100)
        invoice_txt = Entry(self.root, textvariable=self.invoice_var, font=("times new roman", 15), bg="light yellow")
        invoice_txt.place(x=160, y=100, width=180, height=28)

        search_btn = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search)
        search_btn.place(x=360, y=100, width=120, height=28)

        clear_btn = Button(self.root, text="Clear", font=("times new roman", 15, "bold"), bg="light gray", cursor="hand2", command=self.clear)
        clear_btn.place(x=490, y=100, width=120, height=28)

        # ========================================= Bill List =======================================
        sales_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        sales_frame.place(x=50, y=140, width=200, height=330)

        scroll_y = Scrollbar(sales_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scroll_y.set)
        self.sales_list.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.sales_list.yview)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        # ========================================= Bill Area =======================================
        bill_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        bill_frame.place(x=280, y=140, width=410, height=330)

        title_2_lbl = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20, "bold"), bg="orange")
        title_2_lbl.pack(side=TOP, fill=X)

        scroll_y_2 = Scrollbar(bill_frame, orient=VERTICAL)
        scroll_y_2.pack(side=RIGHT, fill=Y)
        self.bill_area = Text(bill_frame, bg="light yellow", yscrollcommand=scroll_y_2.set)
        self.bill_area.pack(fill=BOTH, expand=1)
        scroll_y_2.config(command=self.bill_area.yview)

        # =================================== Image ====================================
        self.bill_photo = Image.open("Images\\cat2.jpg")
        self.bill_photo = self.bill_photo.resize((450, 300))
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        image_lbl = Label(self.root, image=self.bill_photo, bd=0)
        image_lbl.place(x=700, y=110)
        self.show()

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir("Bill\\"):
            if i.split(".")[-1] == "txt":
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split(".")[0])

    def get_data(self, ev):
        index_row = self.sales_list.curselection()
        file_name = self.sales_list.get(index_row)
        self.bill_area.delete('1.0', END)
        f = open(f"Bill\\{file_name}", "r")
        for i in f:
            self.bill_area.insert(END, i)
        f.close()

    def search(self):
        if self.invoice_var.get() == "":
            messagebox.showerror("Error", "Invoice No. is Required", parent=self.root)
        else:
            if self.invoice_var.get() in self.bill_list:
                f = open(f"Bill\\{self.invoice_var.get()}.txt", "r")
                self.bill_area.delete('1.0', END)
                for i in f:
                    self.bill_area.insert(END, i)
                f.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)
        self.invoice_var.set("")


if __name__ == '__main__':
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()
