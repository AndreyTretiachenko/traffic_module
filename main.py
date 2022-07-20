from ftplib import FTP
import requests as rq

def ftp_client():
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


def main():
    request = rq.post("http://{0}:8123".format('127.0.0.1'),
                      params={
        'database': "default",
        'query': "insert into t values (1,1)"
    },
                      headers={
        'X-ClickHouse-User': "default",
        'X-ClickHouse-Key': ""}
                      )
    print(request.text)

if __name__ == '__main__':
    main()


