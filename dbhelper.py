# KDB Helper


version = "1"

def initdb(dbname, xname, yname, compacted=False):
    print("Initializing DataBase")
    with open(f"{dbname}.kdb", "w") as db:
        if not compacted:
            print("* Compaction turned off")
            db.write(f"KasselDB {version} Format\n")
            db.write("2022 Walter Brobson\n")
        db.write(xname + "\n")
        db.write(yname + "\n")
        return 0

def readxdb(dbname, str, compacted=False):
    global xfound
    xfound = False
    with open(f"{dbname}.kdb", "r") as db:
        DB = db.readlines()
        counter = 0
        for line in DB:
            # Boiler Plate stuff....
            counter += 1
            
            if counter < 3:

                continue
            if counter == 3:
                global xname
                xname = line.strip()

                continue
            if counter == 4:
                global yname
                yname = line.strip()

                continue
            
            if counter % 2 == 0 and xfound:
                global result
                result = line.strip()

                return result
            if not counter % 2 == 0:
                if line.strip() == str:
                    xfound = True
                    continue
            
            


