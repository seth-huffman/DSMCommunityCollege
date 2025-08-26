import sqlite3

# After importing the data integration module create a database called weather_tracking
connect = sqlite3.connect("weather_tracking.db")
cursor = connect.cursor()

# In the database, create another table called Location
# The table should have the columns 
#   county (primary key)(text), 
#   state (text)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Location (
    county TEXT PRIMARY KEY,
    state TEXT
)
""")

# In the database, create a table called Precipitation
# The table should have the columns: 
#   location (foreign key to county in Location table), 
#   date (text), 
#   precipitation (float), 
#   precip_type(text)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Precipitation (
    location TEXT,
    date TEXT,
    precipitation REAL,
    precip_type TEXT
)
""")

# Output the database information in the console with your program (table names and column names)
print("Location")
cursor.execute("PRAGMA table_info(Location)")
location = cursor.fetchall()
print(f"- {location[0][1]}")
print(f"- {location[1][1]}")

print("\nPrecipitation")
cursor.execute("PRAGMA table_info(Precipitation)")
precipitation = cursor.fetchall()
print(f"- {precipitation[0][1]}")
print(f"- {precipitation[1][1]}")
print(f"- {precipitation[2][1]}")
print(f"- {precipitation[3][1]}")
