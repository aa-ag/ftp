############------------ IMPORTS ------------############
from ftplib import FTP

############------------ CODE ------------############
# connect to host using default port
# https://www.debian.org/
ftp = FTP('ftp.us.debian.org')

# log into ftp using user authentication
# user anonymous, passwd anonymous@
print(ftp.login())
# 230 Login successful.

print(ftp.cwd('debian'))
# 250 Directory successfully changed.

# list directory contents pre sending file
ftp.retrlines('LIST')

# sends file
file_to_be_sent = open("README", "wb")
ftp.retrbinary('RETR README', file_to_be_sent.write)
print('\n\n -- file sent')

# quits connection
print(ftp.quit())