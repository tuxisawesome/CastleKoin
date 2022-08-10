import dbhelper
import os


#dbhelper.initdb("database", "User", "Coins")
result = dbhelper.readxdb("database", "Walter")
print(result)