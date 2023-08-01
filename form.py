import tkinter
from tkinter import messagebox

if __name__=='__main__':
    window=tkinter.Tk()
    frame=tkinter.Frame()
    frame.configure(bg='#F03A47')
    window.title("Form")
    window.geometry('600x400')
    window.configure(bg='#F03A47')
    def check():
       username = "piu"
       passw="12345p"
       if (entry.get()==username and password_entry.get()==passw):
           messagebox.showinfo(title="Success",message="SuccessFully Logged in")
       else:
           messagebox.showerror(title="Error",message="Invalid Login")
          

    title=tkinter.Label(frame,text="Login",font=("Arial",20),bg='#F03A47',fg='#F6F4F3')
    title.grid(row=0,column=0,columnspan=2,pady=10)
    label=tkinter.Label(frame,text="Username:",font=("Arial",20),bg='#F03A47',fg='#F6F4F3')
    label.grid(row=1,column=0,padx=10)
    entry=tkinter.Entry(frame,font=("Arial",20))
    entry.grid(row=1,column=1,padx=40,pady=40)
    password=tkinter.Label(frame,text="Password:",font=("Arial",20),bg='#F03A47',fg='#F6F4F3')
    password.grid(row=2,column=0)
    password_entry=tkinter.Entry(frame,show="*",font=("Arial",20))
    password_entry.grid(row=2,column=1,padx=40,pady=40)
    button=tkinter.Button(frame,text="Submit",font=("Arial",20),activebackground="#F9EDCC",command=check)
    button.grid(row=3,column=0,columnspan=2)
    frame.pack()
    window.mainloop()
    