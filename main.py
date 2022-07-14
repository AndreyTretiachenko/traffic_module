from ftplib import FTP

def main():
    structure = []
    ftp = FTP("91.122.209.148", "admin", "Admin29")
    ftp.cwd("Counter")
    list_folder = ftp.nlst()
    for l in list_folder:
        ftp.cwd(l)
        city = ftp.nlst()
        structure.append([{'region': l, 'city': city}])
        ftp.cwd("..")
    print(structure[::1])


if __name__ == '__main__':
    main()


