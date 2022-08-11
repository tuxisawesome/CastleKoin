# KDB Helper



version = "1"

def isdblocked():
    with open(f"lockfile.lok", "r") as lock:
        status = lock.readline()
        if status == "L":
            return True
        elif status == "O":
            return False
        else:
            return False

def lockdb():
    with open(f"lockfile.lok", "w") as lock:
        lock.write("L")

def unlockdb():
    with open(f"lockfile.lok", "w") as lock:
        lock.write("O")

def initdb(dbname, xname, yname, compacted=False, locked=True):
    print("Initializing DataBase")
    if locked:
        lockdb()
    else:
        unlockdb()

    if isdblocked():
        print("* Database Locked, not overwriting...")
        return 0
    else:
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
        onenotcomp = True
        counter = 0
        for line in DB:
            # Boiler Plate stuff....
            counter += 1
            if compacted and onenotcomp:
                counter += 2
                onenotcomp = False
                continue
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
        return False
            
def addline(dbname, xname, yname):
    with open(f"{dbname}.kdb", "a") as db:
        db.write(xname + "\n")
        db.write(yname + "\n")



