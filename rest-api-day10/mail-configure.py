import smtplib

try:
    s=smtplib.SMTP("smtp.gmail.com",587)
    sender_email_id="minijainn293@gmail.com" #from
    sender_email_pass="mini1999"
    receiver_email="minijainn99@gmail.com" #to
    message="hello, sending from python smtp"
    s.starttls()
    s.login(sender_email_id,sender_email_pass)
    s.sendmail(sender_email_id,receiver_email,message)
    s.quit()


except Exception as e:
    print(e)


#util-->encrypted file
