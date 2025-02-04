from tkinter import *

window  = Tk()
window.title("Mile to Km convertor")
window.minsize(width=400, height=200)

#Entry
input_miles = Entry(width=30)
input_miles.grid(row=0, column=1)

#Label for Miles
miles = Label(text="Miles", font=("Arial", 16, "bold"))
miles.grid(row=0,column=2)

#Label for KM
km = Label(text="Km", font=("Arial", 16, "bold"))
km.grid(row=1,column=2)

#Lable for is equal to
result_label = Label(text="is equal to", font=("Arial",16, "bold"))
result_label.grid(row=1,column=0)

#Result
result = Label(text="0", font=("Arial", 16, "bold"))
result.grid(row=1,column=1)

def miles_to_km():
    miles = float(input_miles.get())
    km = miles * 1.609
    result["text"] = f"{km:.2f}km"

#Calculate
calculate = Button(text="Calculate", font=("Arial", 16, "bold"), command=miles_to_km)
calculate.grid(row=2,column=1)


window.mainloop()