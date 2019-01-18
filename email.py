#this is how you can interface with an SMTP server using python

from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "spinning.leak@gmail.com"
password = "noneofyourdamnbusiness"
from_email = username
to_list["spinning.leak@gmail.com"]

#creates our connection object
#alternately, you can just import SMPT from smtplib
email_conn = SMTP(host, port)

#acks the server
email_conn.ehlo()

#starts secure layer
email_conn.starttls()

try:
	email_conn.login(username, password)
except SMTPAuthenticationError:
	print("Error logging into SMTP server")

try:
	to_list.append("test@test.ly")

	email_msg = MIMEMultipart("alternative")
	email_msg['Subject'] = "Hi there!"
	email_msg["From"] = from_email
	email_msg["To"] = to_list

	#contains your plain text message
	plain_text_msg = "Test message"

	#contains your HTML based message
	html_msg = """\
		<html>
			<head></head>
			<body>
				<p>Hi there...<br>
					This is a <b>test</b> message
				</p>
			</body>
		</html>
	"""

	part1 = MIMEText(plain_text_msg, 'plain')
	part2 = MIMEText(html_msg, "html"
		
	email_msg.attach(part1)
	email_msg.attach(part2)

	#print(email_msg.as_string())

	email_conn.sendmail(from_email, to_list, email_msg.to_string())

	#you need to quit the connection to the server before you can open another one
	email_conn.quit()
except smtplib.SMTPException:
	print("Error sending message")	

