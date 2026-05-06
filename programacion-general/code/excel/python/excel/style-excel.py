import pandas as pd
from openpyxl.styles import PatternFill, NamedStyle, Alignment, Font, Border, Side
from openpyxl.utils.cell import get_column_letter

dummy_data = [
    {"Date": "2023-01-01", "Region": "North", "Product": "A", "Units Sold": 1000, "Revenue": 10000},
    {"Date": "2023-01-01", "Region": "South", "Product": "B", "Units Sold": 1500, "Revenue": 25000},
    {"Date": "2023-01-02", "Region": "East", "Product": "C", "Units Sold": 800, "Revenue": 12000},
    {"Date": "2023-01-02", "Region": "West", "Product": "A", "Units Sold": 1200, "Revenue": 15000},
    {"Date": "2023-01-03", "Region": "North", "Product": "B", "Units Sold": 900, "Revenue": 18000},
    {"Date": "2023-01-03", "Region": "South", "Product": "C", "Units Sold": 1100, "Revenue": 13000},
    {"Date": "2023-01-04", "Region": "East", "Product": "A", "Units Sold": 1300, "Revenue": 20000},
    {"Date": "2023-01-04", "Region": "West", "Product": "B", "Units Sold": 1000, "Revenue": 15000},
    {"Date": "2023-01-05", "Region": "North", "Product": "C", "Units Sold": 700, "Revenue": 9000},
    {"Date": "2023-01-05", "Region": "South", "Product": "A", "Units Sold": 1800, "Revenue": 28000}
]
# Calculate Variance
for i in range(1, len(dummy_data)):
    current_revenue = dummy_data[i]["Revenue"]
    previous_revenue = dummy_data[i - 1]["Revenue"]
    variance = current_revenue - previous_revenue
    dummy_data[i]["Variance"] = variance
# Create the dataframe
df = pd.DataFrame.from_dict(dummy_data)
# Remove null values
df.fillna(0, inplace=True)

with pd.ExcelWriter("Style-Excel.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sample1", index=False, freeze_panes=(2,0))
    
# Workbook
workbook = writer.book
# Worksheet
worksheet = workbook["Sample1"]

# Insert a column and a row 
# Openpyxl is not zero indexed.
worksheet.insert_cols(1)
worksheet.insert_rows(1)

# Minimize the size of row 1:
worksheet.row_dimensions[1].height= 21.0

worksheet.row_dimensions[1].hidden = True

for column in worksheet.columns:
    max_length = max(len(str(cell.value)) for cell in column)
    adjusted_width = (max_length + 2) * 1.0
    worksheet.column_dimensions[column[0].column_letter].width = adjusted_width
    
# Adjust the size of column "A"
worksheet.column_dimensions["A"].width = 4.0

workbook.close()