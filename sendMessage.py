import smtplib 

from SendOtp import generateOtp
from twilio.rest import Client

from sendMail import sendMail
from sendSMS import sendSMS


def main():
    k = generateOtp()
    # logger.info("your otp is {}".format(k)) s
    s ="your otp is {}".format(k)
    sendMail('virinchi.msk83@gmail.com', '9989796928v', 'virinchi.msk83@gmail.com',s)
    #sendSMS(k , '+919182042514')
    
if __name__=='__main__':
    main()

