import pickle
import hashlib
# Enable file change check
while True:
    try:
        l = pickle.load(open("db"))
    except IOError:
        l = []
    db = dict(l)
    path = "/usr/share/zoneminder/www/scripts/detected"
    #this converts the hash to text
    checksum = hashlib.md5(open(path).read()).hexdigest()
    if db.get(path, None) != checksum:
        db[path] = checksum
        video = open(path).read()
        print video
    pickle.dump(db.items(), open("db", "w"))

