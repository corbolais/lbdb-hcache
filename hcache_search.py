import sqlite3
import sys
import os
import argparse

defaultpath=os.path.expanduser("~/.mutt/address.db")
parser = argparse.ArgumentParser(description='Search for addresses from hcache')
parser.add_argument('terms', metavar='T', type=str, nargs='+',
                   help='search terms')
parser.add_argument('--address-db', dest='dbpath',
                    default=defaultpath,
                    help='Address database to use (default:%s)' % (defaultpath))

args = parser.parse_args()

sqlconn = sqlite3.connect(args.dbpath)

clauses = []
parameters = []
for a in args.terms:
    clauses.append("(name LIKE ? OR email LIKE ?)")
    match = "%%%s%%" % a
    parameters.append(match)
    parameters.append(match)

sql = "select name, email, count(email) AS occurances from addresses WHERE %s GROUP BY email ORDER BY occurances DESC" % (" AND ".join(clauses))
res = sqlconn.execute(sql, parameters)
for r in res.fetchall():
    print "%-30s\t%-30s\t(hcache, %d occurrances)" % (r[1], r[0], r[2])
