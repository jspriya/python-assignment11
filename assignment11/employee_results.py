import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("../db/lesson.db")

# SQL query
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# Load into DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Plot
plt.figure(figsize=(10, 6))
plt.bar(employee_results["last_name"], employee_results["revenue"], color="skyblue")

plt.title("Employee Revenue")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()