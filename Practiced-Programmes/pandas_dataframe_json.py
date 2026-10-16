import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005,
                 1006, 1007, 1008, 1009, 1010],

    "Product": ["Laptop", "Phone", "Shirt", "Shoes", "Rice",
                "Headphones", "Jeans", "Oil", "Keyboard", "T-Shirt"],

    "Category": ["Electronics", "Electronics", "Fashion", "Fashion", "Grocery",
                 "Electronics", "Fashion", "Grocery", "Electronics", "Fashion"],

    "City": ["Hyderabad", "Bengaluru", "Chennai", "Hyderabad", "Bengaluru",
             "Chennai", "Hyderabad", "Chennai", "Hyderabad", "Bengaluru"],

    "Price": [50000, 25000, 3000, 5000, 2000,
              4000, 3500, 1800, 2500, 2200]
}

data_df = pd.DataFrame(data)

print(data_df)

data_df.to_json("D:/Python/Practiced-Programmes/Data/ecommerce.json", orient="records")


