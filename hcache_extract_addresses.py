from pytc import *
import sqlite3
import struct
import StringIO
import datetime
import sys
import os

now = datetime.datetime.now().isoformat(" ")

def dump_char(f):
    size = struct.unpack('i', f.read(4))[0]
    #print "size %d" % size
    if size != 0:
        return f.read(size).decode('utf-8')
    else:
        return None

def dump_addresses(data):
    f = StringIO.StringIO(data)
    f.seek(172)

    addresses = []
    for i in range(0,8):
        num_addr = struct.unpack('i', f.read(4))

        for i in range(0, num_addr[0]):
            name = dump_char(f)
            address = dump_char(f)
            if name:
                addresses.append((name, address))
            f.read(4)
    return addresses

hfile = os.path.expanduser("~/.mutt/cache/headers")
if len(sys.argv) < 2:
    print >> sys.stderr, "Using %s" % hfile
else:
    hfile = sys.argv[1]

bdb = BDB()

sqlconn = sqlite3.connect('example.db')
if sqlconn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='addresses';").fetchone() == None:
    sqlconn.execute("create table addresses (name text, email text, key text, primary key (key, email))")
try:
    bdb.open(hfile, BDBONOLCK | BDBOREADER)
except:
    print >> sys.stderr, "Couldn't open header cache %s" % (hfile)

for k in bdb:
    try:
        addresses = dump_addresses(bdb.get(k))
        for a in addresses:
            try:
                sqlconn.execute("INSERT INTO addresses (name, email, key) VALUES(?, ?, ?)", (a[0], a[1], k))
            except sqlite3.IntegrityError:
                pass # dupe, ignore

    except struct.error:
        pass #this interests me not // it's not a cache entry
sqlconn.commit()
sqlconn.close()
bdb.close()
