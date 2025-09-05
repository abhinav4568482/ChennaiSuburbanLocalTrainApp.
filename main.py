import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def display_ticket():
    # Connect to the database
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Fetch the last booked ticket from the database
    cursor.execute("SELECT * FROM TICKET ORDER BY ROWID DESC LIMIT 1")
    ticket_data = cursor.fetchone()

    if ticket_data:
        # Create a new window to display the ticket
        ticket_window = tkinter.Toplevel()
        ticket_window.title("🎫 Your Ticket - Chennai Suburban Railway")
        ticket_window.configure(bg='#E6F3FF')
        ticket_window.geometry("600x500")
         
        frame = tkinter.Frame(ticket_window, bg='#E6F3FF')
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        user_info_frame = tkinter.LabelFrame(frame, text="🎫 Ticket Information", 
                                           bg='#F0F8FF', fg='#2C3E50', 
                                           font=('Arial', 12, 'bold'),
                                           relief='raised', bd=2)
        user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='ew')
        
        title_label = tkinter.Label(user_info_frame, text="Title", 
                                   bg='#F0F8FF', fg='#34495E', 
                                   font=('Arial', 10, 'bold'))
        title_label.grid(row=0, column=0, padx=10, pady=5)
        
        title_output = tkinter.Label(user_info_frame, text=f"{ticket_data[0]}", 
                                     bg='#F0F8FF', fg='#2C3E50', 
                                     font=('Arial', 10))
        title_output.grid(row=1, column=0, padx=10, pady=5)


        
        first_name_label = tkinter.Label(user_info_frame, text="First Name", 
                                         bg='#F0F8FF', fg='#34495E', 
                                         font=('Arial', 10, 'bold'))
        first_name_label.grid(row=0, column=1, padx=10, pady=5)
        
        first_name_output = tkinter.Label(user_info_frame, text=f"{ticket_data[1]}", 
                                         bg='#F0F8FF', fg='#2C3E50', 
                                         font=('Arial', 10))
        first_name_output.grid(row=1, column=1, padx=10, pady=5)

        
        last_name_label = tkinter.Label(user_info_frame, text="Last Name", 
                                        bg='#F0F8FF', fg='#34495E', 
                                        font=('Arial', 10, 'bold'))
        last_name_label.grid(row=0, column=2, padx=10, pady=5)
        
        last_name_output = tkinter.Label(user_info_frame, text=f"{ticket_data[2]}", 
                                        bg='#F0F8FF', fg='#2C3E50', 
                                        font=('Arial', 10))
        last_name_output.grid(row=1, column=2, padx=10, pady=5)
         
        age_label = tkinter.Label(user_info_frame, text="Age", 
                                   bg='#F0F8FF', fg='#34495E', 
                                   font=('Arial', 10, 'bold'))
        age_label.grid(row=2, column=0, padx=10, pady=5)
        
        age_output = tkinter.Label(user_info_frame, text=f"{ticket_data[3]}", 
                                  bg='#F0F8FF', fg='#2C3E50', 
                                  font=('Arial', 10))
        age_output.grid(row=3, column=0, padx=10, pady=5)
        
        nationality_label = tkinter.Label(user_info_frame, text="Nationality", 
                                         bg='#F0F8FF', fg='#34495E', 
                                         font=('Arial', 10, 'bold'))
        nationality_label.grid(row=2, column=1, padx=10, pady=5)
        
        nationality_output = tkinter.Label(user_info_frame, text=f"{ticket_data[4]}", 
                                         bg='#F0F8FF', fg='#2C3E50', 
                                         font=('Arial', 10))
        nationality_output.grid(row=3, column=1, padx=10, pady=5)
        
        contact_number_label = tkinter.Label(user_info_frame, text="Contact Number", 
                                             bg='#F0F8FF', fg='#34495E', 
                                             font=('Arial', 10, 'bold'))
        contact_number_label.grid(row=2, column=2, padx=10, pady=5)
        
        contact_output = tkinter.Label(user_info_frame, text=f"{ticket_data[5]}", 
                                      bg='#F0F8FF', fg='#2C3E50', 
                                      font=('Arial', 10))
        contact_output.grid(row=3, column=2, padx=10, pady=5)
                
        source_label = tkinter.Label(user_info_frame, text="Source Station", 
                                     bg='#F0F8FF', fg='#34495E', 
                                     font=('Arial', 10, 'bold'))
        source_label.grid(row=4, column=0, padx=10, pady=5)
        
        src_output = tkinter.Label(user_info_frame, text=f"{ticket_data[6]}", 
                                  bg='#F0F8FF', fg='#2C3E50', 
                                  font=('Arial', 10))
        src_output.grid(row=5, column=0, padx=10, pady=5)
        
        destination_label = tkinter.Label(user_info_frame, text="Destination Station", 
                                          bg='#F0F8FF', fg='#34495E', 
                                          font=('Arial', 10, 'bold'))
        destination_label.grid(row=4, column=1, padx=10, pady=5)
        
        dest_output = tkinter.Label(user_info_frame, text=f"{ticket_data[7]}", 
                                   bg='#F0F8FF', fg='#2C3E50', 
                                   font=('Arial', 10))
        dest_output.grid(row=5, column=1, padx=10, pady=5)
        
        route_label = tkinter.Label(user_info_frame, text="Route Type", 
                                    bg='#F0F8FF', fg='#34495E', 
                                    font=('Arial', 10, 'bold'))
        route_label.grid(row=4, column=2, padx=10, pady=5)
        
        route_output = tkinter.Label(user_info_frame, text=f"{ticket_data[8]}", 
                                    bg='#F0F8FF', fg='#2C3E50', 
                                    font=('Arial', 10))
        route_output.grid(row=5, column=2, padx=10, pady=5)
        
        price_label = tkinter.Label(user_info_frame, text="Ticket Price", 
                                    bg='#F0F8FF', fg='#34495E', 
                                    font=('Arial', 10, 'bold'))
        price_label.grid(row=6, column=1, padx=10, pady=5)
        
        price_output = tkinter.Label(user_info_frame, text="₹10", 
                                    bg='#F0F8FF', fg='#27AE60', 
                                    font=('Arial', 12, 'bold'))
        price_output.grid(row=7, column=1, padx=10, pady=5)
        
     
    else:
        tkinter.messagebox.showwarning(title="Error", message="No booked tickets found.")

def Book_Ticket():
    accept = accept_var.get()
    
    if accept == "Booked": 
        #user info get 
        title = title_combobox.get()
        firstName = first_name_entry.get()
        lastName = last_name_entry.get()
        if firstName and lastName :
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            contact = contact_number_Entry.get()
            
            #journey info get
            source = source_combobox.get()
            destination = destination_combobox.get()
            route = route_combobox.get()
            
            #terms and condition info get
            reg_var = accept_var.get() 
            
            print("title : ",title,"firstName : ",firstName , "Last Name : ",lastName)
            print("age : ",age,"Nationality : ",nationality ,"Contact Number : ",contact)
            print("source : ",source,"destination : ",destination,"Route: ",route)
            print("Status : ",reg_var)
            
            #create Table
            conn = sqlite3.connect('test.db')
            table_creation = '''CREATE TABLE IF NOT EXISTS TICKET(title TEXT,
            firstName TEXT, lastName TEXT,age INT,nationality TEXT,
            contact TEXT,source TEXT,destination TEXT,way TEXT)'''
            conn.execute(table_creation)
            
            #insert the data
            insert_data = '''INSERT INTO TICKET(title,firstName,lastName,age,nationality,
                             contact,source,destination,way) VALUES(?,?,?,?,?,?,?,?,?)'''
            insert_data_tuple = (title,firstName,lastName,age,nationality,contact,source,destination,route)                 
            cursor = conn.cursor()
            cursor.execute(insert_data,insert_data_tuple)
            conn.commit()
            conn.close()
            
            tkinter.messagebox.showinfo(title = " Successfully booked" , message = "Your ticket is successfully booked")
            display_ticket()
        else :
            tkinter.messagebox.showwarning(title= "Error",message = "First Name and Last Name are required")    
    else :
       tkinter.messagebox.showwarning(title = "Error",message="You have not accepted the terms and conditions")
        
window = tkinter.Tk()
window.title("Chennai Suburban Ticket Booking")
window.configure(bg='#E6F3FF')  # Light blue background
window.geometry("800x600")  # Set a reasonable window size
window.resizable(True, True)

# Configure style for ttk widgets
style = ttk.Style()
style.theme_use('clam')

frame = tkinter.Frame(window, bg='#E6F3FF')
frame.pack(fill='both', expand=True, padx=20, pady=20)


#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="👤 Passenger Information", 
                                   bg='#F0F8FF', fg='#2C3E50', 
                                   font=('Arial', 12, 'bold'),
                                   relief='raised', bd=2)
user_info_frame.grid(row=0, column=0, padx=20, pady=15, sticky='ew')

title_label = tkinter.Label(user_info_frame, text="Title", 
                               bg='#F0F8FF', fg='#34495E', 
                               font=('Arial', 10, 'bold'),
                               cursor='hand2')
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.","Mrs.","Dr."],
                             font=('Arial', 10),
                             state='readonly')
title_label.grid(row=0, column=0, padx=10, pady=8)
title_combobox.grid(row=1, column=0, padx=10, pady=5)

first_name_label = tkinter.Label(user_info_frame, text="First Name*", 
                                   bg='#F0F8FF', fg='#34495E', 
                                   font=('Arial', 10, 'bold'),
                                   cursor='hand2')
first_name_label.grid(row=0, column=1, padx=10, pady=8)

last_name_label = tkinter.Label(user_info_frame, text="Last Name*", 
                                bg='#F0F8FF', fg='#34495E', 
                                font=('Arial', 10, 'bold'),
                                cursor='hand2')
last_name_label.grid(row=0, column=2, padx=10, pady=8)



first_name_entry = tkinter.Entry(user_info_frame, font=('Arial', 10),
                               relief='solid', bd=1,
                               bg='white', fg='#2C3E50')
first_name_entry.grid(row=1, column=1, padx=10, pady=5)

last_name_entry = tkinter.Entry(user_info_frame, font=('Arial', 10),
                               relief='solid', bd=1,
                               bg='white', fg='#2C3E50')
last_name_entry.grid(row=1, column=2, padx=10, pady=5)

age_label = tkinter.Label(user_info_frame, text="Age", 
                           bg='#F0F8FF', fg='#34495E', 
                           font=('Arial', 10, 'bold'),
                           cursor='hand2')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=5, to=100,
                            font=('Arial', 10),
                            relief='solid', bd=1,
                            bg='white', fg='#2C3E50')
age_label.grid(row=2, column=0, padx=10, pady=8)
age_spinbox.grid(row=3, column=0, padx=10, pady=5)

nationality_label = tkinter.Label(user_info_frame, text="Nationality", 
                                 bg='#F0F8FF', fg='#34495E', 
                                 font=('Arial', 10, 'bold'),
                                 cursor='hand2')
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa","America","Asia","Indian","Europe"],
                                   font=('Arial', 10),
                                   state='readonly')
nationality_label.grid(row=2, column=1, padx=10, pady=8)
nationality_combobox.grid(row=3, column=1, padx=10, pady=5)

contact_number_label = tkinter.Label(user_info_frame, text="Contact Number", 
                                     bg='#F0F8FF', fg='#34495E', 
                                     font=('Arial', 10, 'bold'),
                                     cursor='hand2')
contact_number_label.grid(row=2, column=2, padx=10, pady=8)
contact_number_Entry = tkinter.Entry(user_info_frame, font=('Arial', 10),
                                   relief='solid', bd=1,
                                   bg='white', fg='#2C3E50')
contact_number_Entry.grid(row=3, column=2, padx=10, pady=5)

# Configure grid weights for responsive design
user_info_frame.grid_columnconfigure(0, weight=1)
user_info_frame.grid_columnconfigure(1, weight=1)
user_info_frame.grid_columnconfigure(2, weight=1)

#***********************END OF SECTION USER INFO***************



#JOURNEY INFO

journey_frame = tkinter.LabelFrame(frame, text="🚂 Journey Information", 
                                 bg='#F0F8FF', fg='#2C3E50', 
                                 font=('Arial', 12, 'bold'),
                                 relief='raised', bd=2)
journey_frame.grid(row=1, column=0, sticky='ew', padx=20, pady=15)

source_label = tkinter.Label(journey_frame, text="Source Station", 
                            bg='#F0F8FF', fg='#34495E', 
                            font=('Arial', 10, 'bold'),
                            cursor='hand2')
source_label.grid(row=0, column=0, padx=15, pady=8)

source_combobox = ttk.Combobox(journey_frame, values=["Chennai Park","Tirusulam","Chennai Beach","Potheri","Tambaram","Tambaram Santorium","Chengalpattu","Guindy","Chromepet","Chetpet","Chennai Egmore"],
                              font=('Arial', 10),
                              state='readonly')
source_combobox.grid(row=1, column=0, padx=15, pady=5)

destination_label = tkinter.Label(journey_frame, text="Destination Station", 
                                 bg='#F0F8FF', fg='#34495E', 
                                 font=('Arial', 10, 'bold'),
                                 cursor='hand2')
destination_label.grid(row=0, column=1, padx=15, pady=8)

destination_combobox = ttk.Combobox(journey_frame, values=["Chennai Park","Tirusulam","Chennai Beach","Potheri","Tambaram","Tambaram Santorium","Chengalpattu","Guindy","Chromepet","Chetpet","Chennai Egmore"],
                                   font=('Arial', 10),
                                   state='readonly')
destination_combobox.grid(row=1, column=1, padx=15, pady=5)

route_label = tkinter.Label(journey_frame, text="Route Type", 
                         bg='#F0F8FF', fg='#34495E', 
                         font=('Arial', 10, 'bold'),
                         cursor='hand2')
route_label.grid(row=0, column=2, padx=15, pady=8)

route_combobox = ttk.Combobox(journey_frame, values=["Single","Return"],
                             font=('Arial', 10),
                             state='readonly')
route_combobox.grid(row=1, column=2, padx=15, pady=5)

# Configure grid weights for responsive design
journey_frame.grid_columnconfigure(0, weight=1)
journey_frame.grid_columnconfigure(1, weight=1)
journey_frame.grid_columnconfigure(2, weight=1)
    
#********END OF JOURNEY INFO *************************

#CONFIRMATION

confirmation_frame = tkinter.LabelFrame(frame, text="📋 Terms and Conditions", 
                                       bg='#F0F8FF', fg='#2C3E50', 
                                       font=('Arial', 12, 'bold'),
                                       relief='raised', bd=2)
confirmation_frame.grid(row=2, column=0, sticky='ew', padx=20, pady=15)

confirmation_label = tkinter.Label(confirmation_frame, 
                                 text="⚠️ Once The Ticket Is Booked, It Will Not Be Cancelled", 
                                 bg='#F0F8FF', fg='#E74C3C', 
                                 font=('Arial', 10, 'bold'),
                                 wraplength=400)
confirmation_label.grid(row=0, column=0, padx=15, pady=10)

accept_var = tkinter.StringVar(value="Not Booked")

confirmation_check = tkinter.Checkbutton(confirmation_frame,
                                        text="✅ I accept the terms and conditions*",
                                        variable=accept_var,
                                        onvalue="Booked",
                                        offvalue="Not Booked", 
                                        bg='#F0F8FF', fg='#34495E',
                                        font=('Arial', 10, 'bold'),
                                        cursor='hand2')
confirmation_check.grid(row=1, column=0, padx=15, pady=10)

# Configure grid weights for responsive design
confirmation_frame.grid_columnconfigure(0, weight=1) 
     
#*************END OF CONFIRMATION*****************
   
   
        
#BOOK TICKET BUTTON

#BOOK TICKET BUTTON
def on_button_hover(event):
    button.config(bg='#27AE60', relief='raised')

def on_button_leave(event):
    button.config(bg='#2ECC71', relief='flat')

button = tkinter.Button(frame, text="🎫 Book Ticket", 
                       bg='#2ECC71', foreground='white', 
                       font=('Arial', 12, 'bold'),
                       relief='flat', bd=0,
                       padx=30, pady=10,
                       cursor='hand2',
                       command=Book_Ticket)
button.grid(row=3, column=0, pady=20)

# Bind hover effects
button.bind('<Enter>', on_button_hover)
button.bind('<Leave>', on_button_leave)

# Designer Credit - At the very bottom - SUPER VISIBLE
credit_frame = tkinter.Frame(frame, bg='#E74C3C', relief='raised', bd=3)
credit_frame.grid(row=4, column=0, pady=25, padx=20, sticky='ew')

credit_label = tkinter.Label(credit_frame, text="Designed by Abhinav", 
                             bg='#E74C3C', fg='white', 
                             font=('Arial', 18, 'bold'),
                             cursor='hand2',
                             padx=40,
                             pady=20)
credit_label.pack()

# Add a test label to make sure it's visible
test_label = tkinter.Label(frame, text="TEST - This should be visible", 
                          bg='yellow', fg='black', 
                          font=('Arial', 12, 'bold'))
test_label.grid(row=5, column=0, pady=10, sticky='ew')





window.mainloop()