#import SMTP library
#yoy will need to use pip to install it using the command pip intsall smtp
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS to secure message
s.starttls()
 
# Authentication
#use gmail apps password and not your actual gmail password login
s.login("my_email ", "sender_email_password")
 
# message to be sent
message = "I managed to plot the graph using data from the csv files you sent me!"
 
# sending the mail
s.sendmail("my_email ", "coworker_email", message)
 
# terminating the session
s.quit()
