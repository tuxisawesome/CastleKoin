import dbhelper
import os


dbhelper.initdb("database", "User", "Coins")
dbhelper.addline("database","Walter","600")
result = dbhelper.readxdb("database", "Walter")
if not result:
    print("Not there!")
else:
    print(result)