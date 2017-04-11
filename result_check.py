from twilio.rest import TwilioRestClient #SMS API Package
import urllib.request
import re
import time
 #using Twilio
account_sid = "" #Your Twilio account ID
auth_token = ""    #Your secret API Token

client = TwilioRestClient(account_sid, auth_token)

while 1:

    html_content = urllib.request.urlopen('http://www.exam.dtu.ac.in/result.htm').read() #result page url

    match1 = re.findall("B.Tech. V Semester", str(html_content)); #RegEx to find the keywords
    match2= re.findall("613", str(html_content)) 


    if len(match1) == 0:
       print("Yeah, Result Not Declared. Going to sleep") #will not send anything
       time.sleep(900) #sleep for 1 hour

    else:
       msg = client.messages.create(to="+9199999999", from_="", body="Oops! Resutls out, Best of Luck. ") #Will send SMS to your phone number
       print("SMS Sent Thanks")
       quit()