import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.wind(return_type='pandas')

# Print first 10 rows
print("First 10 rows:")
print(df.head(10))

# Print last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))

# Clean data: convert 'strength' to float
df["strength"] = df["strength"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Strength vs Frequency",
    labels={"frequency": "Frequency", "strength": "Wind Strength"}
)

# Save to HTML
fig.write_html("wind.html")

print("\nPlot saved as wind.html")

# Open in browser automatically (optional)
fig.show()


