import pandas as pd

# Daten erstellen
data = {'Name': ['Max', 'Lisa', 'Tom', 'Julia'],
        'Alter': [28, 32, 45, 41],
        'Stadt': ['Berlin', 'Hamburg', 'München', 'Köln']}

# DataFrame erstellen
df = pd.DataFrame(data)

# DataFrame anzeigen
print(df)
