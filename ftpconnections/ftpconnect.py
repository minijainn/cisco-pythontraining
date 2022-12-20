import ftplib
hostname="ftp.dlptest.com"
username="dlpuser"
password="rNrKYTX9g7z3RgJRmxWuGHbeu"
print("con start")
ftp_server=ftplib.FTP(hostname,username,password)
print("con end")
ftp_server.encoding="utf-8"
fileName="abc.txt"
with open(fileName,"rb") as file:
    ftp_server.storbinary(f"STOR {fileName}",file)

ftp_server.dir()
ftp_server.quit()
