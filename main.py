from ftplib import FTP

def main():
    structure = [{
        'region': ['region'],
        'city': [{'region': 'region1', 'city': ['city1', 'city2', 'city3']},
                 {'region': 'region2', 'city': ['city2', 'city3', 'city4']},
                 {'region': 'region3', 'city': ['city5', 'city6', 'city7']}],
        'company': [{'city': 'city1', 'company': ['company1', 'company2', 'company3']},
                    {'city': 'city2', 'company': ['company4', 'company5', 'company6']}],
        'shops': [{'city': 'city1', 'shops': ['shop1', 'shop2', 'shop3']},
                  {'city': 'city2', 'shops': ['shop4', 'shop5', 'shop6']}],
        'device': [{'shop': 'shop1', 'devices': ['device1']},
                   {'shop': 'shop2', 'devices': ['device2', 'device2']}]
    }]
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


