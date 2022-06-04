from tkinter import *

root = Tk()
root.title("Tuples")
root.geometry("400x400")

month = ("January", "February", "March", "April", "May", "June", "July", "August", 
         "September", "October", "Novenber", "December")

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

max_profits = max(profits)
max_profit_index = profits.index(max_profits)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The Maximum Profit Of : " + str(max_profits) + " Was Recorded In The Month Of " + str(max_profit_month))

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
print(min_profits_index)

min_profit_month = month[min_profits_index]
print("The Minimum Profit Of : " + str(min_profits) + " Was Recorded In The Month Of : " + str(min_profit_month))

root.mainloop()

