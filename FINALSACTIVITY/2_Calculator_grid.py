import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("240x280")
window.title("Calculator")

#History
history_entry = tk.Entry(window, justify= RIGHT,width= 26)
history_entry.insert(0,"5 * 5 = 25" )

#Output
output_entry = tk.Entry(window, justify= RIGHT,)
output_entry.insert(0,"5")

#Grid of History and Output
history_entry.grid(row = 0, column = 0, pady = 2, columnspan = 4)
output_entry.grid(row = 1, column = 0, pady = 2, columnspan = 4)

#---------------------------------------------------

#Row 2
button_7 = tk.Button(window, text="7", width= 5)
button_8 = tk.Button(window, text="8", width= 5)
button_9 = tk.Button(window, text="9", width= 5)
button_div = tk.Button(window, text="/", width= 5)

#Row 3
button_4 = tk.Button(window, text="4", width= 5)
button_5 = tk.Button(window, text="5", width= 5)
button_6 = tk.Button(window, text="6", width= 5)
button_mul = tk.Button(window, text="*", width= 5)

#Row 4
button_1 = tk.Button(window, text="1", width= 5)
button_2 = tk.Button(window, text="2", width= 5)
button_3 = tk.Button(window, text="3", width= 5)
button_sub = tk.Button(window, text="-", width= 5)

#Row 5
button_clear = tk.Button(window, text="C", width= 5)
button_0 = tk.Button(window, text="0", width= 5)
button_equ = tk.Button(window, text="=", width= 5)
button_add = tk.Button(window, text="+", width= 5)

#---------------------------------------------------
#Grid

#Row 2
button_7.grid(row = 2, column = 0, pady = 5 )
button_8.grid(row = 2, column = 1, pady = 5 )
button_9.grid(row = 2, column = 2, pady = 5 )
button_div.grid(row = 2, column = 3, pady = 5 )

#Row 3
button_4.grid(row = 3, column = 0, pady = 5 )
button_5.grid(row = 3, column = 1, pady = 5 )
button_6.grid(row = 3, column = 2, pady = 5 )
button_mul.grid(row = 3, column = 3, pady = 5 )

#Row 4
button_1.grid(row = 4, column = 0, pady = 5 )
button_2.grid(row = 4, column = 1, pady = 5 )
button_3.grid(row = 4, column = 2, pady = 5 )
button_sub.grid(row = 4, column = 3, pady = 5 )

#Row 5
button_clear.grid(row = 5, column = 0, pady = 5 )
button_0.grid(row = 5, column = 1, pady = 5 )
button_equ.grid(row = 5, column = 2, pady = 5 )
button_add.grid(row = 5, column = 3, pady = 5 )

#---------------------------------------------------
label = tk.Label(window, text="Calculator Mo To!")
label.grid (row= 6, column=0, columnspan=4)

window.mainloop()