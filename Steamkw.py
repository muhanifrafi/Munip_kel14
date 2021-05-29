from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginFrame)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)



        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)



    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "abc" and password == "123":
            self.parent.switch_frame(PageOne)
        else:
            tm.showerror("Login error", "Incorrect username or password")
class PageOne(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Pilih game yang diinginkan").pack(side="top", fill="x", pady=10)
        self.bg = PhotoImage(file = "G:\\Download\\rdr2(1).png")
        label1 = Label( self, image = self.bg)
        label1.place(x = 0, y = 0)
        hasil = IntVar()
        R1 = Radiobutton(self, text="Red dead redemption 2", variable=hasil, value=500000,
                  )
        R1.pack( anchor = W )

        R2 = Radiobutton(self, text="Resident evil", variable=hasil, value=600000,
                  )
        R2.pack( anchor = W )

        R3 = Radiobutton(self, text="PUBG", variable=hasil, value=700000,
                  )
        R3.pack( anchor = W)
        tk.Button(self, text="Return to login page",
                  command=lambda: parent.switch_frame(LoginFrame)).pack()
        tk.Button(self, text="Saran list game selanjutnya ",
                  command=lambda: parent.switch_frame(Pagetwo)).pack()
        def munip():
            tm.showinfo("Bayar","Barang yang anda beli adalah sebanyak "+str(hasil.get()))
        tk.Button(self, text="Beli",
                  command=munip).pack()
class Pagetwo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Pilih listgame yang ingin ada disini").pack(side="top", fill="x", pady=10)
        stack = []
        listgame=StringVar()
        game = Entry(self,textvariable=listgame).pack()
        def masukdata():
            stack.append(listgame.get())
            print ("")
        def pencet():
            if stack ==[]:
                tm.showinfo("data kosong","masukan data terlebih dahulu")
            else:
                n=1
                for i in stack:
                    tm.showinfo("harapan game","Semoga nanti saya akan menambahkan listgame anda\n"+i)
        tk.Button(self, text="harapan game baru",
                  command=masukdata).pack()
        tk.Button(self, text="submit",
                  command=pencet).pack()
        tk.Button(self, text="Return to login page",
                  command=lambda: parent.switch_frame(LoginFrame)).pack()
        tk.Button(self, text="Beli game",
                  command=lambda: parent.switch_frame(Pageone)).pack()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
