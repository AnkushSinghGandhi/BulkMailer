import smtplib



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(maildid, password)
    
    subject = "Test"
    Body = """
    Hello Testing!!!!
    """
    message = f'Subject{subject}\n\n\n{Body}'
    
    smtp.sendmail(maildid, maildid, message)