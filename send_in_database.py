import datetime

import requests as rq
import datetime as dtime

body_1 = {"serial_number": "70-b3-d5-1a-05-48", "dateTime": "2022-07-21 15:43",
        "passReport": [{"id": 1,
                        "passList": [
                            {"passType": 2, "time": "15:43:33"},
                            {"passType": 1, "time": "15:45:55"}
                        ]
                        },
                        {"id": 2,
                        "passList": [
                            {"passType": 2, "time": "16:01:33"},
                            {"passType": 1, "time": "16:55:55"}
                        ]
                        }
                       ]
        }


def parse_body(body):
    data = []
    for report in body['passReport']:
        for l in report['passList']:
            data.append({"serial_number": body["serial_number"],
                         "dateTime": body["dateTime"],
                         "pass_type": l["passType"],
                         "pass_time": l["time"]})
    return data


def send_request(body_request):
    data_body = parse_body(body_request)
    if len(data_body) != 0:
        for data in data_body:
            print(f"INSERT INTO traffic (serial_number, dateTime, pass_type, pass_time) VALUES ('{data['serial_number']}', {dtime.datetime.strptime(data['dateTime'], '%Y-%m-%d %H:%M')})")
            request = rq.post("http://192.168.0.43:8123",
                              params={
                                  "database": "vladykin",
                                  "query": f"INSERT INTO traffic (serial_number, dateTime, pass_type, pass_time) VALUES ('123', '{dtime.datetime.strptime(data['dateTime'], '%Y-%m-%d %H:%M')}', {data['pass_type']}, '{dtime.time.strptime(data['dateTime'], '%H:%M:%S')}')"
                              }
                              )
            print(request.text)

    return



def main():
    send_request(body_1)



if __name__ == "__main__":
    main()