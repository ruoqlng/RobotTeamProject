import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

def main():

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Patrick's Cell Phone")

    main_frame = ttk.Frame(root, padding=100, relief='raised')
    main_frame.grid()

    name_tag = ttk.Label(main_frame, text="Keypad")
    name_tag.config(font=('Courier',30))
    name_tag.grid(row=0, column=2)

    num_buttom_1 = ttk.Button(main_frame, text="1")
    num_buttom_1.grid(row=2, column = 1)
    num_buttom_1['command'] = (lambda: num_entry.insert(0, "1"))
    num_buttom_2 = ttk.Button(main_frame, text="2")
    num_buttom_2.grid(row=2, column=2)
    num_buttom_2['command'] = (lambda: num_entry.insert(0, "2"))
    num_buttom_3 = ttk.Button(main_frame, text="3")
    num_buttom_3.grid(row=2, column=3)
    num_buttom_3['command'] = (lambda: num_entry.insert(0, "3"))
    num_buttom_4 = ttk.Button(main_frame, text="4")
    num_buttom_4.grid(row=3, column=1)
    num_buttom_4['command'] = (lambda: num_entry.insert(0, "4"))
    num_buttom_5 = ttk.Button(main_frame, text="5")
    num_buttom_5.grid(row=3, column=2)
    num_buttom_5['command'] = (lambda: num_entry.insert(0, "5"))
    num_buttom_6 = ttk.Button(main_frame, text="6")
    num_buttom_6.grid(row=3, column=3)
    num_buttom_6['command'] = (lambda: num_entry.insert(0, "6"))
    num_buttom_7 = ttk.Button(main_frame, text="7")
    num_buttom_7.grid(row=4, column=1)
    num_buttom_7['command'] = (lambda: num_entry.insert(0, "7"))
    num_buttom_8 = ttk.Button(main_frame, text="8")
    num_buttom_8.grid(row=4, column=2)
    num_buttom_8['command'] = (lambda: num_entry.insert(0, "8"))
    num_buttom_9 = ttk.Button(main_frame, text="9")
    num_buttom_9.grid(row=4, column=3)
    num_buttom_9['command'] = (lambda: num_entry.insert(0, "9"))
    num_buttom_asterisk = ttk.Button(main_frame, text="*")
    num_buttom_asterisk.grid(row=5, column=1)
    num_buttom_asterisk['command'] = (lambda: num_entry.insert(0, "*"))
    num_buttom_0 = ttk.Button(main_frame, text="0")
    num_buttom_0.grid(row=5, column=2)
    num_buttom_0['command'] = (lambda: num_entry.insert(0, "0"))
    num_buttom_pound_sign = ttk.Button(main_frame, text="#")
    num_buttom_pound_sign.grid(row=5, column=3)
    num_buttom_pound_sign['command'] = (lambda: num_entry.insert(0, "#"))
    call_buttom = ttk.Button(main_frame, text="call")
    call_buttom.grid(row=6, column=2)
    num_entry = ttk.Entry(main_frame, width=20)
    num_entry.grid(row=1,column=2)





    root.mainloop()

main()