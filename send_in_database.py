import requests as rq

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
            request = rq.post("192.168.0.37:8123",
                              params={
                                  "database": "test",
                                  "query": f"INSERT INTO traffic VALUES ("
                                           f"{data['serial_number']}, {data['dateTime']}, {data['pass_type']}, {data['pass_time']}"
                              }
                              )
            print(request.text)

    return



def main():
    send_request(body_1)



if __name__ == "__main__":
    main()