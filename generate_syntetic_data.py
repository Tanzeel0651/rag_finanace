import pandas as pd
import numpy as np

# Generate synthetic financial data for different types of reports

# 1. Income Statement Data
income_statement = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "Revenue (in millions)": [500, 550, 600],
    "Cost of Goods Sold (COGS) (in millions)": [200, 220, 250],
    "Gross Profit (in millions)": [300, 330, 350],
    "Operating Expenses (in millions)": [150, 160, 170],
    "Net Income (in millions)": [150, 170, 180]
})

# 2. Balance Sheet Data
balance_sheet = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "Assets (in millions)": [1000, 1100, 1200],
    "Liabilities (in millions)": [500, 520, 540],
    "Equity (in millions)": [500, 580, 660]
})

# 3. Cash Flow Statement Data
cash_flow_statement = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "Operating Cash Flow (in millions)": [200, 220, 240],
    "Investing Cash Flow (in millions)": [-100, -120, -140],
    "Financing Cash Flow (in millions)": [50, 70, 90],
    "Net Cash Flow (in millions)": [150, 170, 190]
})

# Save the datasets as CSV files for structured data retrieval
income_statement.to_csv("data/income_statement.csv", index=False)
balance_sheet.to_csv("data/balance_sheet.csv", index=False)
cash_flow_statement.to_csv("data/cash_flow_statement.csv", index=False)

# 4. Financial Summaries (Unstructured Data)
financial_summaries = """
2022 Summary: The company experienced a revenue increase of 10% compared to the previous year, 
reaching $500 million. Gross profit margin remained stable at 60%, and net income grew to $150 million.

2023 Summary: Continued growth led to revenue reaching $550 million, supported by strong operational efficiencies. 
Net income increased by 13.3% year-over-year, showcasing improved profitability.

2024 Summary: Revenue reached $600 million, driven by increased market penetration. 
The company's net income stood at $180 million, reflecting strategic investments and cost optimizations.
"""

# Save financial summaries as a text file
with open("data/financial_summaries.txt", "w") as file:
    file.write(financial_summaries)

# 5. Sample Queries and Expected Retrievals
#sample_queries = [
#    {"query": "What was the revenue in 2023?", "retrieved_data": "Revenue for 2023 was $550 million."},
#    {"query": "What is the company's net income trend?", "retrieved_data": "Net income grew from $150M in 2022 to $170M in 2023 and $180M in 2024."},
#    {"query": "What are the key financial highlights of 2024?", "retrieved_data": "Revenue: $600M, Net Income: $180M, improved profitability."}
#]
#
## Save sample queries as JSON
#import json
#with open("data/sample_queries.json", "w") as file:
#    json.dump(sample_queries, file, indent=4)


