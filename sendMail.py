import smtplib
import logging 


logging.basicConfig(filename="msgfile.log",format=' %(levelname)s %(asctime)s %(message)s %(funcName)s %(lineno)d ', filemode='a') 
logger=logging.getLogger(name='send-mail') 
logger.setLevel(logging.INFO)
# logging.basicConfig(filename="newfile.log", 
#                     format='%(asctime)s %(message)s', 
#                     filemode='a')

def sendMail(mailId, password, toMail, msg):
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    try:
        mailServer.starttls()
    except smtplib.SMTPHeloError:
        print(" The server didn’t reply properly to the HELO greeting.")
    except smtplib.SMTPNotSupportedError:
        print("The command or option attempted is not supported by the server.")
    else:
        try:
            mailServer.login(mailId , password)
        except smtplib.SMTPHeloError:
            print("The server didn't reply properly to the HELO greeting.")
        except smtplib.SMTPAuthenticationError:
            print("The server didn't accept the username/password combination.")
        except smtplib.SMTPNotSupportedError:
            print("The AUTH command is not supported by the server.")
        else:
            logger.info("Logged into  {}".format(mailId))
            # print( mailServer.verify(toMail))
            try:
                mailServer.sendmail(mailId, toMail , msg)
            except smtplib.SMTPServerDisconnected:
                print("This exception is raised when the server unexpectedly disconnects, or when an attempt is made to use the SMTP instance before connecting it to a server.")
            except smtplib.SMTPResponseException:
                print("Base class for all exceptions that include an SMTP error code")
            except smtplib.SMTPSenderRefused:
                print("Sender address refused. In addition to the attributes set by on all SMTPResponseException exceptions, this sets ‘sender’ to the string that the SMTP server refused")
            except smtplib.SMTPRecipientsRefused:
                print("All recipient addresses refused. The errors for each recipient are accessible through the attribute recipients") 
            except smtplib.SMTPDataError:
                print("The SMTP server refused to accept the message data.")
            except smtplib.SMTPConnectError:
                print("Error occurred during establishment of a connection with the server.")
            except smtplib.SMTPHeloError:
                print("The server refused our HELO message.")
            except smtplib.SMTPNotSupportedError:
                print("The command or option attempted is not supported by the server")
            except smtplib.SMTPAuthenticationError:
                print("SMTP authentication went wrong. Most probably the server didn’t accept the username/password combination provided.")
            else:            
                logger.info("Mail sent to {} from {}".format(toMail,mailId ))
                mailServer.quit()

# def main():
#     sendmail('virinchi.msk83@gmail.com', '9989796928v', 'virinchi.msk83@gmail.com','learning python')
# if __name__=='__main__':
#      main()