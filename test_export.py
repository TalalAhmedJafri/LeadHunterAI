from exports.excel_export import export_leads

sample_data = [
    ("Optimum Nutrition", "https://optimumnutrition.com", "USA", "New"),
    ("MyProtein", "https://myprotein.com", "USA", "New"),
    ("Transparent Labs", "https://transparentlabs.com", "USA", "New"),
]

export_leads(sample_data)

print("Excel file created successfully!")