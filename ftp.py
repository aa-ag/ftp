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