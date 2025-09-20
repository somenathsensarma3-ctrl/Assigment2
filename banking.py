import pandas as pd

# --- 1. Education: Student Average Marks ---
students = pd.DataFrame({
    "Name": ["Riya","Karan","Meena"],
    "Maths": [80, 75, 90],
    "Science": [85, 70, 88]
})
students["Average"] = students[["Maths","Science"]].mean(axis=1)
print("Education Data:\n", students, "\n")

# --- 2. Banking: Balance Calculation ---
bank = pd.DataFrame({
    "Customer": ["Amit","Priya","Rahul"],
    "Deposit": [5000, 7000, 6000],
    "Withdraw": [2000, 1500, 1000]
})
bank["Balance"] = bank["Deposit"] - bank["Withdraw"]
print("Bank Data:\n", bank, "\n")

# --- 3. Retail: Sales Revenue ---
sales = pd.DataFrame({
    "Product": ["Laptop","Mobile","Tablet"],
    "Units": [5, 10, 7],
    "Price": [40000, 15000, 20000]
})
sales["Revenue"] = sales["Units"] * sales["Price"]
print("Retail Data:\n", sales)
