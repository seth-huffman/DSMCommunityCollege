import sqlite3
import shutil
from datetime import datetime, timedelta

# Create a copy of your database (You can do this in Python or whatever way you prefer)
shutil.copyfile("weather_tracking.db", "copied.db")
connect = sqlite3.connect("copied.db")
cursor = connect.cursor()

# If you used inches for your original precipitation, read them in from your 
# database and replace them with millimeters.  Do the opposite if you started with millimeters.
cursor.execute("SELECT rowid, precipitation FROM Precipitation")
for rowid, inches in cursor.fetchall():
    millimeters = inches * 25.4
    cursor.execute("UPDATE Precipitation SET precipitation = ? WHERE rowid = ?", (millimeters, rowid))

# Make the date on each of your readings 1 day earlier (because you realized the reading date was actually the day after the actual precipitation)
cursor.execute("SELECT rowid, date FROM Precipitation")
for rowid, date in cursor.fetchall():
    new = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    cursor.execute("UPDATE Precipitation SET date = ? WHERE rowid = ?", (new, rowid))

# Delete one of your cities and all of the data associated with it.
cursor.execute("DELETE FROM Precipitation WHERE location = ?", ("Fairfield",))
cursor.execute("DELETE FROM Location WHERE county = ?", ("Fairfield",))

# Finalize changes
connect.commit()
connect.close()
