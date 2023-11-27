import smtplib


def send_automatic_email():
    user = input("Enter your username: ")
    email = input("Enter your gmail: ")
    message = f"Dear {user}, Welcome to PVC Solution Corp..."
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("toiyeuhong@gmail.com", "qrnkievdwujgaxxb")
    s.sendmail("PVC Group", email, message)
    print("Email sent!!!")


send_automatic_email()
