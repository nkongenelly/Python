import MySQLdb
import time

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","","pythontweets")

c = conn.cursor()

username='python'

tweet='it is working'

c.execute("INSERT INTO tweets (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

conn.commit()