import tkinter as tk
from tkinter import ttk

def calculate_startup_cost():
    try:
        total_cost = 0
        for field_name, entry in entries.items():
            value = float(entry.get())

            #Prevent negative or zero inputs
            if value < 0:
                result_label.config(text=f"❌ Error: '{field_name}' must be a positive number!", fg="red")
                return

            total_cost += value

        # ✅ Display results
        result_label.config(
            text=f"💵 Total Startup Cost: ${total_cost:,.2f}",
            fg="green"
        )

    except ValueError:
        result_label.config(text="❌ Please enter valid numeric values!", fg="red")

#Create main application window
root = tk.Tk()
root.title("Startup Cost Calculator")
root.geometry("700x500")
root.resizable(False, False)

#Title Label
title_label = tk.Label(root, text="Startup Cost Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Fields for different startup costs
fields = {
    "Business Registration and Legal Fees": None,
    "Website Platform Fees": None,
    "Initial Inventory Fees": None,
    "Initial Packaging and Shipping Costs": None,
    "Initial Branding Costs": None,
    "Initial Marketing Costs": None,
    "Initial Software Subscriptions Costs": None,
    "Initial Insurance Costs": None,
    "Total Initial Capital Needed (3-6 months of operating expenses)": None
}

entries = {}

#Use grid layout for better UI
frame = tk.Frame(root)
frame.pack(pady=10)

for i, (label_text, _) in enumerate(fields.items()):
    tk.Label(frame, text=f"{label_text}:", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label_text] = entry

#Calculate Button
calculate_button = tk.Button(root, text="Calculate Startup Cost", command=calculate_startup_cost, bg="blue", fg="white", font=("Arial", 12))
calculate_button.pack(pady=10)

#Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

#Run the application
root.mainloop()
