# tutorial  https://www.youtube.com/watch?v=QVyAeM12wVY
# https://en.wikipedia.org/wiki/List_of_FTP_commands

from ftplib import FTP
ftp = FTP('ftp.phonomena.net')
ftp.login(user='phonomena.net', passwd='phonotez.23')
welcomessage = ftp.getwelcome()
print(">>> " + welcomessage)
ftp.set_debuglevel(1)
ftp.cwd('/pragma/')
print("Current Directory >>> " + ftp.pwd())
ftp.dir()
# flist = ftp.retrlines('LIST ')
# print("flist >> " + flist)


#  FP003-INFOSHEET.pdf


def grabFile(thisfile):
    filename = thisfile
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()


def placeFile(thisfile):
    filename = thisfile  # 'testUpload.pdf'
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))


def makeDir(newdir):

    if(ftp.mkd(newdir) == "550 Can't create directory: File exists"):
        print("TERRORRRRR")
    else:
        print("OKKKKKKKKK")
        # ftp.mkd(newdir)

    # print(" TRESPONSE ::: " + ftp.mkd(newdir))
    # if(ftp.cwd(newdir)):
    #     ftp.mkd(newdir)clear
    # else:
    #     print("directory already exists!!!")

    # ftp.cwd(newdir)
    # print("list >> " + ftp.retrlines('LIST '))


print('========== ******** ============')
folderName = 'xdirectory'
if folderName in ftp.nlst():
    print('folder already exists')
else:
    print('xxxxxxxxxxxxx=======xxxxxxxxxxx')
    ftp.mkd(folderName)
    print('new folder ' + folderName + " created")

ftp.cwd(folderName + "/")
print("Current Directory >>> " + ftp.pwd())

placeFile('testUpload.pdf')
ftp.dir()

# print("list >> " + ftp.retrlines('LIST '))

ftp.quit()
