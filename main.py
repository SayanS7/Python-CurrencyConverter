from forex_python.converter import CurrencyRates
from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('900x350+350+115')
root.title("Currency Convertor Application")
root.config(background="light grey")
header_font = ("Verdana", 16, "bold")
font = ("Times New Roman", 16)
bg = PhotoImage(file="img/currency.png")
photoLabel = Label(root, image=bg)
photoLabel.place(x=0, y=0, relwidth=1, relheight=1)

# some variable declaration
amount1 = StringVar(root)

variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("From Country")
variable2.set("To Country")


# important functions

def createWidget():
    country_list = ['India(INR)', 'United States of America(USD)', 'Canada(CAD)', 'China(CNY)', 'Denmark(DKK)',
                    'European Union(EUR)', 'Japan(JPY)', 'Czech Republic(CZK)', 'Australia(AUD)', 'Norway(NOK)',
                    'Mexican (MXN)', 'Malaysia(MYR)', 'Hungary(HUF)', 'Brazil(BRL)', 'Poland(PLN)', 'Romania(RON)',
                    'Sweden(SEK)', 'United Kingdom(GBP)', 'Switzerland(CHF)','New Zealand(NZD)']

    text_label = Label(root, text="Welcome to Python Currency Converter", font=header_font, bg='lavender')
    text_label.grid(row=1, column=1, pady=10)

    amount_label = Label(root, text="Enter amount :  ", font=font)
    amount_label.grid(row=2, column=0, pady=10)

    global amount_entry1
    amount_entry1 = Entry(root, width=30, textvariable=amount1, font=font, justify=CENTER, bg='lavender')
    amount_entry1.grid(row=2, column=1, pady=10)

    
    from_country = Label(root, text="From Country: ", font=font)
    from_country.grid(row=3, column=0, padx=5, pady=10)

    from_menu = OptionMenu(root, variable1, *country_list)
    from_menu.grid(row=3, column=1, padx=20, pady=10)

    to_country = Label(root, text="To Country: ", font=font)
    to_country.grid(row=4, column=0, padx=5, pady=10)

    to_menu = OptionMenu(root, variable2, *country_list)
    to_menu.grid(row=4, column=1, padx=20, pady=10)

    convert_btn = Button(root, width=10, text="Convert", command=calculate, font=font, relief="ridge")
    convert_btn.grid(row=4, column=2, padx=20, pady=10)

    converted_text = Label(root, text="Converted Amount : ", font=font)
    converted_text.grid(row=5, column=0, padx=20, pady=10)

    global amount_entry2
    amount_entry2 = Entry(root, width=30, font=font, justify=CENTER, bg='lavender')
    amount_entry2.grid(row=5, column=1, pady=10)

    clear_btn = Button(root, text="Clear", width=10, command=all_clear, font=font, relief="ridge")
    clear_btn.grid(row=5, column=2, padx=20, pady=10)


def String_Split(inData):
    x = inData.find("(", 1)
    y = inData.find(")", x)
    return inData[x + 1:y]


def calculate():
    c = CurrencyRates()

    var1_full = variable1.get()
    var1 = String_Split(var1_full)
    var2_full = variable2.get()
    var2 = String_Split(var2_full)
    print(var1)
    print(var2)

    if amount_entry1.get() == "":
        tkinter.messagebox.showerror("Error", "Amount Not Entered.\n")

    elif var1 == "From Countr" or var2 == "To Countr":
        tkinter.messagebox.showerror("Error", "Currency Not Selected.\n")

    else:
        new_amt = c.convert(var1, var2, float(amount_entry1.get()))
        new_amount = float("{:.2f}".format(new_amt))
        print(new_amount)
        amount_entry2.insert(0, str(new_amount))


def all_clear():
    amount_entry2.delete(0, END)
    amount_entry1.delete(0, END)
    variable1.set("From Country")
    variable2.set("To Country")


# end of functions


createWidget()

root.mainloop()
