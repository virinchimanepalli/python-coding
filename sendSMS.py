import logging


from twilio.rest import Client


logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s  %(funcName)s %(lineno)d ') 
logger=logging.getLogger(name='send-sms') 
logger.setLevel(logging.INFO)

def sendSMS(text, toNum):
    # account_sid = os.environ['ACCOUNT_SID']
    # auth_token = os.environ['AUTH_TOKEN']
    account_sid = 'AC7cbf38c45c0733d099e227ab26610a19'
    auth_token = '3b89aa89cc7323564ab5c7dc527f904e'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body= text,
                                from_='+17656130238',
                                to= toNum
                            )
    logger.info("SMS sent to {} with sid {}".format(toNum,message.sid))
    return message.sid

# def main():
#     # sendSMS('happy diwali from virinchi', '+919182042514')
# if __name__=='__main__':
#     main()

#ADD DOCSTRINGS