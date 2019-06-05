# from urllib import request
import requests
import ssl
import os

base_url = "https://test.gongtongti.com.cn"

app_login_url = "/v1/customer/auth/login"

manage_login_url = "/v1/common/manage/login"

get_code_url = "/v1/customer/code/get_code"

new_list_url = "/v1/customer/notice/new_list"

all_permission = "/v1/manage/system/user/role/show"

gov_permission = "/v1/government/system/user/role/show"

change_role_url = "/v1/customer/auth/change_gov_role"

permission_list = "/v1/government/system/permission/all/index"

token = "qk95MYDiC7z5cM8N"
city_id = "330700"

customer_id = "658"

# 接口的参数
params = {
    # "admin_token": token,
    "token": token,
    "city_id": city_id,
}
version = "1.1.3"
organization_id = ""
village_id = "63"
platform = "android"
code = ""
mobile = "13634133426"

type = 2

# 添加基本的字典


def getParams(params):
    params['platform'] = platform
    params['village_id'] = village_id
    params['token'] = token
    return params

# 获取权限
def getPermission(url):
    r = requests.get(url, getParams(params))
    x = r.headers
    print(str(r.url))
    print(str(x)+"/n/n")
    print(r.text)


def getPermissionList():
    r = requests.get(base_url+permission_list, getParams(params))
    x = r.headers
    print(str(r.url))
    print(str(x)+"/n/n")
    print(r.json())

# 获取验证码


def get_code():
      url = base_url+get_code_url
      code_params = {
          "mobile": mobile,
      }
      r = requests.get(url, code_params)
      x = r.headers
      print(str(x)+"/n/n")
      print(r.text)


def app_loign(url):
    print("app_loign")
    mobiles = "13634133426"
    login_params = {
        "mobile": mobiles,
        "code": "1234",
        "password": "",
        "platform":"android"
    }
    get_code_params = {
        "mobile": mobiles,
    }

    r_get_code = requests.post(base_url+get_code_url, get_code_params)
    print(r_get_code.json())

    r = requests.post(url, login_params)
    print(r.request.method)
    print(r.request.body)
    x = r.headers

    print("headers--->", r.headers)
    print("url--->", r.url)
    print(r.json())
    print(r.encoding)

# 登录


def login(url):
    login_params = {
        "name": "xiongyisen",
        "password": "123456789",
        "platform": "manage"
    }

    r = requests.post(url, login_params)
    print(r.request.method)
    print(r.request.body)
    x = r.headers

    print("headers--->", r.headers)
    print("url--->", r.url)
    print(r.json())
    print(r.encoding)
    # json()

def get_new_list(url):
    login_params = {
        "category_id": "1",
        # "keywords": "乡",
        "page": "1",
        "per_page": "100"
    }
    r = requests.get(url, getParams(login_params))
    print(r.request.method)
    print(r.request.body)
    x = r.headers

    print("headers--->", r.headers)
    print("url--->", r.url)
    print(r.json())
    print(r.encoding)

# 更换角色
def changeRole(type):
    url = base_url+change_role_url
    login_params = {
        "type": type,
    }
    r = requests.post(url,  getParams(login_params))
    print(r.text)
    pass


if __name__ == "__main__":
    if(type == 0):
        login(base_url+manage_login_url)
    elif(type == 1):
        app_loign(base_url+app_login_url)
        pass
    elif(type == 2):
        get_new_list(base_url+new_list_url)
    elif(type == 3):
        getPermissionList()

    pass
