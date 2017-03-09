from __future__ import print_function
from rdoclient import RandomOrgClient
r=RandomOrgClient("0c39b793-4783-42d1-ae19-c465c076fa9b")
x=r.generate_integers(5,0,10)
y=x[1]
print(y)