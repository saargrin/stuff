#!/usr/bin/python


import argparse
import ldap

parser = argparse.ArgumentParser(description='domain operations')
parser.add_argument('execid', type=str, help='execid')
parser.add_argument('customer', type=str, help='customer')
parser.add_argument('operation', type=str, help='operation')

args = parser.parse_args()

customer = args.customer
operation = args.operation

connect = ldap.initialize('ldap://domain.com')
connect.protocol_version = ldap.VERSION3
connect.set_option(ldap.OPT_REFERRALS, 0)



def findComputer(connect,customer):
 base_dn = 'DC=domain,DC=com'
 criteria = "(&(objectClass=computer))"
 retrieveAttributes = ["distinguishedName"]
 filter = str("cn="+customer)
 try:
  res=connect.search_s(base_dn, ldap.SCOPE_SUBTREE,filter,retrieveAttributes)
 except Exception as v: 
  print (v)
 results = [entry for dn, entry in res if isinstance(entry, dict)] 
 return (results)  

def recursive_delete(conn, base_dn):
    search = conn.search_s(base_dn, ldap.SCOPE_ONELEVEL)

    for dn, _ in search:
        recursive_delete(conn, dn)

    print ("Deleting: ", base_dn)
    conn.delete_s(base_dn)

def deleteComputer(connect,customer) :
 deleteDN = "OU=test522,OU=Computers,DC=domain,DC=com"
 print ("will delete",deleteDN)
 try:
  recursive_delete(connect,deleteDN)
 except Exception as e: #ldap.LDAPError as e:
  print (e)
  
try:
 connect.simple_bind_s('CN=username,OU=InternalUsers,OU=users,DC=domain,DC=com', 'password')
except Exception as v:
	print (v)

### find example
'''result =  (findComputer(connect,customer))
print (result)
'''

deleteComputer(connect,customer)



 



