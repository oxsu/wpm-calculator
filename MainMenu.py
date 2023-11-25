import tkinter

def info(): #Info Page
    test.withdraw() #when info button is clicked, the main menu is hidden
    new_window = tkinter.Toplevel(test)
    new_window.configure(background='#55423d')
    new_window.title("Info Page")
    new_window.geometry("650x350")
    new_window.resizable(False, False)

    info_text = ("We made this App/Project to calculate the speed of your Typing. Typing faster has a lot of beneficial to us.\n"
                 "Here is the example:\n\n"
                 "1. Typing speed is crucial in the workplace because it directly impacts productivity and efficiency.\n\n"
                 "2. A skilled typist is able to finis h a writing task within a specific"
                 "length of time and is not\n hindered by their slower typing speed.\n\n"
                 "3. Candidates who learn to type faster are more favourable to employers.\n\n"
                 "4. It guarantees that they can produce more text for the company (and in less time).\n\n"
                 "5. Makes it Easier to Take Notes\n\n"
                 "6. Typing helps activate new memory muscles and build more active and strong cognitive connections "
                 "\nthat in turn will enhance your overall brain capacity and function.\n")

    info_label = tkinter.Label(new_window, text=info_text, justify="left", font=("Arial", 10), bg="#55423d", fg="#fff3ec")
    info_label.pack()

    def main_menu():
        new_window.withdraw()
        test.deiconify()

    back_button = tkinter.Button(new_window, text='<<Back to Main Menu>>', command=main_menu, bg="#ffc0ad") #Main Menu Button
    back_button.pack()

test = tkinter.Tk()
test.configure(background='#55423d')
test.title("WPM Typing Test")
test.geometry("650x350")
test.resizable(False, False)

button1 = tkinter.Button(test, font='bold', text='START', width=25, height=3, bg="#ffc0ad", fg="#271c19") #Start Button
button2 = tkinter.Button(test, font='bold', text='INFO', width=25, height=3, bg="#ffc0ad" , fg="#271c19", command=info) #Info Button

button1.place(x=220, y=70)
button2.place(x=220, y=180)
test.mainloop()