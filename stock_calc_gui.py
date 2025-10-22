import tkinter as tk
from tkinter import messagebox

# 1. СТРУКТУРА ДАНИХ (ВАШ ОНОВЛЕНИЙ СЛОВНИК)
products_list = {
    "HG224" : {
        "HG223" : 2,
        "HG222" : 2,
        "HG221" : 1,
        "HG214-SUP" : 1,
        "HG951" : 1,
        
    },
    "HG209" : {
        "HG211" : 5,
        "HG213-SUP" : 1,
        "HG951" : 1,
    
    },
}

# 2. ФУНКЦІЯ РОЗРАХУНКУ (ВАША ФУНКЦІЯ, перекладена на англ.)
def calculate_parts_of_products(name: str, number: int) -> dict:
    parts_total = {}
    
    # Використовуємо UPPERCASE для перевірки, оскільки GUI перетворюватиме ввід
    upper_name = name.upper() 
    
    if upper_name in products_list:
        # Тут 'key' перейменовано на 'quantity_per_item' для кращої читабельності
        for product, quantity_per_item in products_list[upper_name].items(): 
            total_needed = int(quantity_per_item) * number
            parts_total[product] = total_needed
        return parts_total
    else:
        return {}

# 3. ФУНКЦІЯ, ЯКА ОБРОБЛЯЄ ПОДІЇ ВІД GUI
def perform_calculation():
    """
    Отримує дані з полів GUI, виконує розрахунок та виводить результат.
    """
    
    # 1. Отримання та очищення вводу
    product_code = entry_code.get().strip().upper() # Автоматично переводимо у верхній регістр
    quantity_str = entry_quantity.get().strip()
    
    # 2. Валідація кількості
    try:
        quantity = int(quantity_str)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Quantity must be a positive integer.") # Помилка вводу
        return
        
    # 3. Виконання розрахунку
    results = calculate_parts_of_products(product_code, quantity)
    
    # 4. Виведення результатів
    if not results:
        # Обробка випадку, коли код продукції не знайдено
        available_codes = ', '.join(products_list.keys())
        messagebox.showerror("Error", f"Product code '{product_code}' not found.\nAvailable: {available_codes}")
        return
    
    # Форматування тексту звіту
    report_text = f"Calculation for {quantity} units of {product_code}:\n\n"
    for part, total_quantity in results.items():
        report_text += f"{part}: {total_quantity} pcs.\n"
        
    # Вивід результату у спливаючому вікні
    messagebox.showinfo("Components Report", report_text)


# 4. НАЛАШТУВАННЯ ГРАФІЧНОГО ІНТЕРФЕЙСУ (GUI)

# Ініціалізація головного вікна
root = tk.Tk()
root.title("Stock Composition Calculator") # Назва вікна
root.geometry("400x200") # Розмір вікна
root.resizable(False, False) # Заборона зміни розміру

# --- Інформаційна Мітка ---
info_label = tk.Label(root, text="Enter product code and quantity:", font=("Arial", 10, "bold")) # Мітка
info_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)


# --- Поле для Коду ---
label_code = tk.Label(root, text="Product Code:") # Мітка
label_code.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_code = tk.Entry(root, width=20)
entry_code.grid(row=1, column=1, padx=10, pady=5)
# Встановлюємо перший код зі списку як приклад
entry_code.insert(0, list(products_list.keys())[0]) 


# --- Поле для КІлькості ---
label_quantity = tk.Label(root, text="Quantity of Units:") # Мітка
label_quantity.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_quantity = tk.Entry(root, width=20)
entry_quantity.grid(row=2, column=1, padx=10, pady=5)
entry_quantity.insert(0, "1")


# --- Кнопка Розрахунку ---
button_calculate = tk.Button(
    root, 
    text="CALCULATE COMPOSITION", # Текст кнопки
    command=perform_calculation, 
    bg="#2e8b57", # Зелений колір
    fg="white", 
    font=("Arial", 10, "bold")
)
button_calculate.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

# Запуск головного циклу застосунку
root.mainloop()