import sqlite3
import matplotlib.pyplot
from datetime import datetime, timedelta

# Import this data into your program
connect = sqlite3.connect("weather_tracking.db")
cursor = connect.cursor()

# Write this data to your database tables in the Location and Precipitation tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Location (
    county TEXT PRIMARY KEY,
    state TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Precipitation (
    location TEXT,
    date TEXT,
    precipitation REAL,
    precip_type TEXT
)
""")

# Gather weather data from at least two different counties for a range of 30 days
cursor.execute("INSERT INTO Location VALUES ('Ottumwa', 'Iowa')")
cursor.execute("INSERT INTO Location VALUES ('Fairfield', 'Iowa')")

for i in range(30):
    date = (datetime(2025, 6, 16) + timedelta(days=i)).strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO Precipitation VALUES (?, ?, ?, ?)", ("Ottumwa", date, i + 1, i + 1))
    cursor.execute("INSERT INTO Precipitation VALUES (?, ?, ?, ?)", ("Fairfield", date, i - 1, i - 1))

connect.commit()

cursor.execute("SELECT date, precipitation FROM Precipitation WHERE location = 'Ottumwa'")
placeOne = cursor.fetchall()
cursor.execute("SELECT date, precipitation FROM Precipitation WHERE location = 'Fairfield'")
placeTwo = cursor.fetchall()

connect.close()

dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in placeOne]
precipitationOne = [row[1] for row in placeOne]
precipitationTwo = [row[1] for row in placeTwo]

# Now bring this data back into your program to create a visual of the precipitation data
matplotlib.pyplot.plot(dates, precipitationOne, label="Ottumwa")
matplotlib.pyplot.plot(dates, precipitationTwo, label="Fairfield")

matplotlib.pyplot.xlabel("Date")
matplotlib.pyplot.ylabel("Precipitation")
matplotlib.pyplot.show()



