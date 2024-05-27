#!/usr/bin/env python3
from tkinter import Label, Tk, Button, Toplevel

import rospy
from std_msgs.msg import Int32

x = None

# Function to handle the button click events
def open_page(page_title):
    global x
    if page_title == "interaction":
        x = 1
    elif page_title == "Navigation":
        x = 2
    elif page_title == "x":
        x = 3
    elif page_title == "y":
        x = 4
    pub.publish(x)

    

rospy.init_node('gui', anonymous=True)
pub = rospy.Publisher('button_topic', Int32, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz

root = Tk()
root.title('Interactive Upper Humanoid')
root.geometry('925x500+300+200')
root.configure(bg="white")
root.resizable(False, False)

button1 = Button(root, text="interaction", font=("Arial", 12), bg="white", command=lambda: open_page("interaction"))
button1.pack(pady=20)

button2 = Button(root, text="Navigation", font=("Arial", 12), bg="white", command=lambda: open_page("Navigation"))
button2.pack(pady=20)

button3 = Button(root, text="x", font=("Arial", 12), bg="white", command=lambda: open_page("x"))
button3.pack(pady=20)

button4 = Button(root, text="y", font=("Arial", 12), bg="white", command=lambda: open_page("y"))
button4.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

