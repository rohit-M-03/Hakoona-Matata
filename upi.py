
from bhimupipy import verify_upi

import sys

def process_arguments(args):
  
    if len(args) > 1:
        global upivalue
        upi_id = args[1]
        print("UPI ID passed as argument:", upi_id)
        a=verify_upi(upi_id)
        upivalue=a["data"]["vpaValid"]
       
    else:
        print("No UPI ID provided as argument.")

def main():
    process_arguments(sys.argv)

if __name__ == "__main__":
    main()
