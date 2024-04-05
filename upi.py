
from bhimupipy import verify_upi

def upi(st):
    global upivalue
    a=verify_upi(st)
    upivalue=a["data"]["vpaValid"]

def upicheck(st):
    return upi(st)
    
if __name__ == "__main__":
    st=sys.argv[0]
    upi(st)
