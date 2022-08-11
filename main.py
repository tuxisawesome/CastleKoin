import dbhelper


print("* Server is starting")

dbhelper.initdb("usercoins", "Users", "Coins", False, False)
dbhelper.initdb("userpass", "Users", "Pass", False,False)
dbhelper.lockdb()