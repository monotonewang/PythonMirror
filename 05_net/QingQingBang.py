# from urllib import request
import requests
import ssl
import os

base_url = "https://test.goingtowin.com"

login_url = "/v1/customer/auth/gov_login"

get_code_url = "/v1/customer/code/get_code"

all_permission = "/v1/manage/system/user/role/show"

gov_permission = "/v1/government/system/user/role/show"

change_role_url="/v1/customer/auth/change_gov_role"

token = "TCA6mD3MtT8wnBMphN"
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
platform = "Android"
code = ""
mobile = "13634133426"

type = 1

# 添加基本的字典
def getParams(params):
    params['customer'] = customer_id
    params['platform'] = platform
    params['version'] = version
    params['city_id'] = city_id
    if(organization_id.strip() != ''):
        params['organization_id'] = organization_id
    return params

# 获取权限
def getPermission(url):
    r = requests.get(url, getParams(params))
    x = r.headers
    print(str(r.url))
    print(str(x)+"/n/n")
    print(r.text)

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

# 登录
def login(url):

    login_params = {
        "city_id": city_id,
        "mobile": mobile,
        "code": "1234",
        "password": ""
    }

    r = requests.post(url, login_params)
    x = r.headers
    file2 = open("token.txt", 'w')
    file2.write(str(x))
    file2.close()

    file = open("mobile.txt", 'w')
    file.write(r.text)
    file.close()
    print("url--->",r.url)
    print(r.text)
    json=r.json()
    json()


# 更换角色
def changeRole(type):
    url=base_url+change_role_url
    login_params = {
        "type": type,
    }
    r = requests.post(url,  getParams(login_params))
    print(r.text)
    pass


if __name__ == "__main__":
    if(type == 0):
        get_code()
    elif(type == 1):
        login(base_url+login_url)
    elif(type == 2):
        getPermission(base_url+gov_permission)

    pass
