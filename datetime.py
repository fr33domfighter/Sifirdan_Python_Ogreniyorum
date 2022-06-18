from datetime import datetime
from datetime import timedelta
simdi = datetime.now()
dogumgunu = datetime(2005,4,17)
result = datetime.timestamp(dogumgunu)
t = dogumgunu - simdi 
t = t.days
print(result)
print(t)