
#!/usr/bin/python

import threading
import sivmware
import pymysql
import ConfigParser



# =============== setup =====
config = ConfigParser.ConfigParser()
config.read("/etc/ansible/.rundeck.conf")
hostname = 'il-rundeck01'
musername = config.get("rundeck","username")
password = config.get("rundeck","password")
database = config.get("rundeck","database")

try:
 DBC = pymysql.connect( host=hostname, user=musername, passwd=password, db=database )
 CUR=DBC.cursor()
except pymysql.InternalError as error:
 code, message = error.args
 print ('>>>>>>>>>>>>>', code, message)


DC = "ny"
SI = sivmware.getSI(DC)

# =============== functions ==========



def getStoppedVMs(dc):
 vms = []
 query = 'select customer from POC where stopped = 1 and region = %s'
 try:
  CUR.execute( query ,dc)
  rows  = CUR.fetchall()
  for row in rows:
   vms.append(row[0])
  return (vms)
 except pymysql.InternalError as error:
  code, message = error.args
  print (">>>>>>>>>>>>>", code, message)
  return (False)


def getStatusofVMS(number,vms):
 for j in range(number*2,(number*2)+2):
  vmname = vms[j]
  print "checking",vmname
  isAlive = sivmware.findSingleVMbyName(vmname,DC,SI)
  if isAlive:
   lineitem = str("thread:"+str(number)+" VM:"+vmname)
   LIVEVMS.append(lineitem)
  if not isAlive:
   lineitem = str("thread:"+str(number)+" VM:"+vmname)
   DEADVMS.append(lineitem)











#========================= main

LIVEVMS = []
DEADVMS = []

vms = getStoppedVMs(DC)

thread_list = []

for i in range(0,10):
    t = threading.Thread(target=getStatusofVMS,args=(i,vms))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print "Done"
print LIVEVMS
print DEADVMS
