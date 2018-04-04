import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

me = 'useriraj2000@gmail.com'
password = '??????'
server = 'smtp.gmail.com:587'
you = 'i.norouzi@parspooyesh.com'

text = """
Hello, Friend.

Here is your data:

{table}

Regards,

Me"""

html = """
<html>
<head>
</head>
<body>
{table}
<table  border="1" style="width:100%" align="center" bgcolor="#00FF00">
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Points</th>
  </tr>
  <tr>
    <td align="center">Jill</td>
    <td align="center">Smith</td>
    <td align="center">50</td>
  </tr>
  <tr>
    <td align="center">Eve</td>
    <td align="center">Jackson</td>
    <td align="center">94</td>
  </tr>
</table>

</body>
</html>

"""

with open('input.csv') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))

message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])

message['Subject'] = "Your data"
message['From'] = me
message['To'] = you
server = smtplib.SMTP(server)
server.ehlo()
server.starttls()
server.login(me, password)
server.sendmail(me, you, message.as_string())
server.quit()
