import os
import math
import random
import smtplib

digits="0123456789"
temp_OTP=""
#otp=".join([str(random(0,9)for i in range(6))])"
for i in range(6):
    temp_OTP+=digits[math.floor(random.random()*10)]
otp = temp_OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("email", "app_password_google")
emailid = input("Enter your email: ")
s.sendmail('vanageshreyu@gmail.com',emailid,msg)
a = input("Enter Your OTP >>: ")
if a==temp_OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
