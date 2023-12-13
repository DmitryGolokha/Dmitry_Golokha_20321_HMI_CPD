import tkinter as tk
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Учет и анализ расходов")

        self.date_label = tk.Label(self.window, text="Дата:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack()

        self.category_label = tk.Label(self.window, text="Категория:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self.window)
        self.category_entry.pack()

        self.amount_label = tk.Label(self.window, text="Сумма:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        self.add_button = tk.Button(self.window, text="Добавить", command=self.add_expense)
        self.add_button.pack()

        self.expense_list = tk.Listbox(self.window)
        self.expense_list.pack()

        self.delete_button = tk.Button(self.window, text="Удалить", command=self.delete_expense)
        self.delete_button.pack()

        self.plot_button = tk.Button(self.window, text="Построить график", command=self.plot_expenses)
        self.plot_button.pack()

        self.window.mainloop()

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        expense = f"Дата: {date}, Категория: {category}, Сумма: {amount}"
        self.expense_list.insert(tk.END, expense)

    def delete_expense(self):
        selected_index = self.expense_list.curselection()
        if selected_index:
            self.expense_list.delete(selected_index)

    def plot_expenses(self):
        dates = []
        categories = []
        amounts = []

        for expense in self.expense_list.get(0, tk.END):
            parts = expense.split(",")
            date = parts[0].split(": ")[1]
            category = parts[1].split(": ")[1]
            amount = float(parts[2].split(": ")[1])
            
            dates.append(date)
            categories.append(category)
            amounts.append(amount)

        plt.bar(categories, amounts)
        plt.xlabel("Категория")
        plt.ylabel("Сумма")
        plt.title("Расходы по категориям")
        plt.show()

expense_tracker = ExpenseTracker()