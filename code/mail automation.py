import smtplib
from tkinter import filedialog
from tkinter import *
from string import Template
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders

from tkinter import filedialog
from tkinter import *
import pandas as pd
import numpy as np
from statistics import mean

MY_ADDRESS = 'fjdjfhj@gmail.com'
PASSWORD = '*******'
dict={}
dict4={}
ccl=[]
global folder_path
global folder_path1
z = []
uns = []
need = []
ex = []
obt = []
z1=[]
na=[]
global folder_path2

def check():
    a = var4.get()
    print(a)
    b = var5.get()
    print(b)
    Receiver = Label(root, text="Choose the college")
    Receiver.grid(row=4, column=0)
    drop = OptionMenu(root,var1,*dict)
    drop.grid(row = 4,column = 1)
    Check = Checkbutton(root, text="cc", variable=var2).grid(row=4, column = 2)
    button4 = Button(text="Add cc", command=ok)
    button4.grid(row=5, column=2)
    if(a==1 and b ==1):
        attach()
    if(a==1):
        event()
def event():
    try:
        print(z1)
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        name = var1.get()
        email = dict[name] 
        message_template = read_template('eventt.txt')
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        sub = message.split('\n', 1)[0]
        message = '\n'.join(message.split('\n')[1:])
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Cc']=",".join(ccl)
        msg['Subject']= sub
        msg.attach(MIMEText(message, 'plain'))
        if z1 is not None:
            for each_file_path in z1:
                try:
                    file_name=each_file_path.split("/")[-1]
                    print(file_name)
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(each_file_path, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                    msg.attach(part)
                except:
                    print ("could not attache file")
        s.send_message(msg)
        print(message)
        del msg
        s.quit()
    except:
        print("Choose the user")
    
def attach():

    global folder_path1
    filename = filedialog.askopenfilename()
    folder_path1.set(filename)
    z1.append(filename)
    button3 = Button(text="attach more", command=attach)
    button3.grid(row=12, column=2)
    a = var4.get()
    if(a == 1):
        print("entered evene")
        submit = Button(root, text="Send Email", fg="Black", 
                                bg="Blue", command=event)
        submit.grid(row=12, column=1)
        
    else:
        submit = Button(root, text="Send Email", fg="Black", 
                                bg="Blue", command=mail) 
        submit.grid(row=12, column=1)
    

  
def browse_button():
    global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    z.append(filename)
    data()
    
def data():
    un = 0
    n = 0
    e = 0
    a = IDEAL_field1.get()
    na.append(a)
    print(na)
    filename = z[0]
    data = pd.read_csv(filename)
    score=data["CodeKata Score"]
    df = pd.DataFrame(score)
    print(df.isnull().sum())
    df = df.fillna(0)
    l=len(df)
    o = int(np.nanmean(score))
    a=float(IDEAL_field1.get())
    print(a)
    u =float(a*(60/100))
    n1 =float(a*(99/100))
    print(a)
    for i in range(0,l):
        if(score[i]<=u):
            un+=1
        if(score[i]>=u and score[i]<=n1):
            n+=1
        if(score[i]>=a):
            e+=1
    
    uns.append(un)
    need.append(n)
    ex.append(e)
    obt.append(o)
    print('Exceede'+str(e))
    print('needs'+str(n))
    print('unsatisfied'+str(un))
    main()
    
def main():
    root.configure(background='light green') 
    root.title("SENDING REPORT") 
    root.geometry("700x300")
    folder_path = StringVar()
    button2 = Button(text="Browse", command=browse_button)
    button2.grid(row=0, column=3)

    
    Receiver = Label(root, text="Choose the college", bg="light green")   
    drop = OptionMenu(root,var1,*dict)
    drop.grid(row = 1,column = 1)
    
    Check = Checkbutton(root, text="cc", variable=var2).grid(row=8, sticky=W)
    
   
    heading = Label(root, text="Report", bg="light green") 
    OBTAINED = Label(root, text="Obtained Avg Expected Codekata Score this week", bg="light green") 
    US = Label(root, text="Unsatisfactory category count", bg="light green") 
    NEEDS = Label(root, text="Needs imporvement category count", bg="light green") 
    EXCEEDED = Label(root, text="Exceeded Expectation Category count", bg="light green") 
    Receiver.grid(row=0, column=0) 
    OBTAINED.grid(row=4, column=0) 
    US.grid(row=5, column=0) 
    NEEDS.grid(row=6, column=0) 
    EXCEEDED.grid(row=7, column=0) 
    OBTAINED_field = Label(root, text= obt[0] , bg="light green") 
    US_field = Label(root, text= uns[0] , bg="light green") 
    NEEDS_field = Label(root, text= need[0] , bg="light green")  
    EXCEEDED_field = Label(root, text= ex[0], bg="light green") 
    OBTAINED_field.grid(row=4, column=1, ipadx="100") 
    US_field.grid(row=5, column=1, ipadx="100") 
    NEEDS_field.grid(row=6, column=1, ipadx="100") 
    EXCEEDED_field.grid(row=7, column=1, ipadx="100") 
    
    submit = Button(root, text="Submit", fg="Black", 
                            bg="Red", command=ok) 
    submit.grid(row=8, column=1)  
    folder_path1 = StringVar()
    attach1 = Button(text="Attach", command=attach)
    attach1.grid(row = 8, column = 2)
    root.mainloop
    
def mail():
    print(z1)
    a = na[0]
    b = obt[0]
    c = uns[0] 
    d = need[0] 
    e = ex[0]
    f = Batch_field1.get()
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    name = var1.get()
    email = dict[name] 
    message_template = read_template('message.txt')
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title(),IDEAL = a ,OBTAINED = b, US = c,NEEDS = d, EXCEEDED = e,BATCH = f,DATE = d1)
    sub = message.split('\n', 1)[0]
    message = '\n'.join(message.split('\n')[1:])
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Cc']=",".join(ccl)
    msg['Subject']= sub
    msg.attach(MIMEText(message, 'plain'))
    if z1 is not None:
        for each_file_path in z1:
            try:
                file_name=each_file_path.split("/")[-1]
                print(file_name)
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(each_file_path, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
                msg.attach(part)
            except:
                print ("could not attache file")
    s.send_message(msg)
    print(message)
    del msg
    s.quit()
    
def ok():
    print(var1.get())
    f= var2.get()
    
    if(f == 1):
        names1, emails1 = get_cccontacts('cc.txt')
        for name1, email1 in zip(names1, emails1):
            dict4[name1] = email1
        Label(root, text="Choose the List of cc", bg="light green").grid(row =10,sticky=W) 
        drop = OptionMenu(root,var3,*dict4)
        drop.grid(row = 11, column = 1)
        button = Button(root, text="Add", command=Add)
        button.grid(row =11, column = 2)
    else:
        return f

def Add():
    g=var3.get()
    h=dict4[g]
    ccl.append(h)
    print(ccl)

def get_cccontacts(filename):
    names1 = []
    emails1 = []
    
    
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names1.append(a_contact.split()[0])
            emails1.append(a_contact.split()[1])
            
    
    return names1, emails1

def get_contacts(filename):
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

    return names, emails

def read_template(filename):

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
def close_window():
    root.destroy()

if __name__ == '__main__':
    names, emails = get_contacts('client.txt')
    for name, email in zip(names, emails):
        dict[name] = email

    
    root = Tk()
    root.title("ABC")
    var1 = StringVar(root)
    var2 = IntVar()
    var3 = StringVar(root)
    var4 = IntVar()
    IDEAL1 = Label(root, text="Ideal Avg Expected Codekata Score this week")
    IDEAL1.grid(row=2, column=0)
    IDEAL_field1 = Entry(root)
    IDEAL_field1.grid(row=2, column=1, ipadx="100")
    Batch = Label(root, text="Batch")
    Batch.grid(row=3, column=0)
    Batch_field1 = Entry(root)
    Batch_field1.grid(row=3, column=1, ipadx="100") 
    folder_path = StringVar()
    button2 = Button(text="Browse", command=browse_button)
    button2.grid(row=0, column=3)
    Check = Checkbutton(root, text="event", variable=var4).grid(row=0, sticky=W)
    
    var5 = IntVar()
    var6 =StringVar(root)
    folder_path = StringVar()
    folder_path1 = StringVar()
    Check = Checkbutton(root, text="attachment", variable=var5).grid(row=1, sticky=W)
    button3 = Button(text="submit", command=check)
    button3.grid(row=1, column=3)
    button31 = Button(text="Quit", command=close_window)
    button31.grid(row=2, column=3)





