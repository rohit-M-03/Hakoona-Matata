
from bhimupipy import verify_upi

def upi(st):
    global upivalue
    a=verify_upi(st)
    upivalue=a["data"]["vpaValid"]

def upicheck(st):
    return upi(st)

st = "1234"
print(upi(st))