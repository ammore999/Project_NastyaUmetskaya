import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


root = tk.Tk()
root.title("Testform")
root.geometry("400x480")
'''name'''
label_name = tk.Label(root, text="Name")
label_name.grid(row=0, column=0, sticky="w", padx=20, pady=10)

entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, sticky="w", padx=10, pady=10)

'''pasvord'''''
label_pass = tk.Label(root, text="Password")
label_pass.grid(row=1, column=0, sticky="w", padx=20, pady=10)

'''шов скрывает пароль'''
entry_pass = tk.Entry(root, width=25, show="*")
entry_pass.grid(row=1, column=1, sticky="w", padx=10, pady=10)

'''sex'''
label_gender = tk.Label(root, text="Gender")
label_gender.grid(row=2, column=0, sticky="nw", padx=20, pady=5)


gender_var = tk.StringVar(value="Male")

rb_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
rb_male.grid(row=2, column=1, sticky="w", padx=10)

rb_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
rb_female.grid(row=3, column=1, sticky="w", padx=10)

'''kontinent'''
label_continent = tk.Label(root, text="Continent")
label_continent.grid(row=4, column=0, sticky="w", padx=20, pady=10)

'''spisok'''''
combo_continent = ttk.Combobox(root, width=22, state="readonly")
combo_continent["values"] = ("Please select...", "Europe", "Asia", "Africa", "North America")
combo_continent.current(0)
combo_continent.grid(row=4, column=1, sticky="w", padx=10, pady=10)

'''eat'''
label_meals = tk.Label(root, text="Meals")
label_meals.grid(row=5, column=0, sticky="nw", padx=20, pady=5)

'''galochki'''
meal_bf = tk.BooleanVar()
meal_ln = tk.BooleanVar()
meal_dn = tk.BooleanVar()

cb_breakfast = tk.Checkbutton(root, text="breakfast", variable=meal_bf)
cb_breakfast.grid(row=5, column=1, sticky="w", padx=10)

cb_lunch = tk.Checkbutton(root, text="lunch", variable=meal_ln)
cb_lunch.grid(row=6, column=1, sticky="w", padx=10)

cb_dinner = tk.Checkbutton(root, text="dinner", variable=meal_dn)
cb_dinner.grid(row=7, column=1, sticky="w", padx=10)

'''zametki'''
label_remark = tk.Label(root, text="Remark")
label_remark.grid(row=8, column=0, sticky="nw", padx=20, pady=10)

'''pole'''
text_remark = tk.Text(root, width=25, height=4)
text_remark.grid(row=8, column=1, sticky="w", padx=10, pady=10)


'''knopki'''
def on_send():

    messagebox.showinfo("Success", "Form submitted successfully!")


def on_cancel():
    '''zakrivaem'''
    root.destroy()



frame_buttons = tk.Frame(root)
frame_buttons.grid(row=9, column=1, sticky="e", padx=10, pady=10)

btn_send = tk.Button(frame_buttons, text="Send", width=8, command=on_send)
btn_send.pack(side="left", padx=5)

btn_cancel = tk.Button(frame_buttons, text="Cancel", width=8, command=on_cancel)
btn_cancel.pack(side="left", padx=5)


root.mainloop()