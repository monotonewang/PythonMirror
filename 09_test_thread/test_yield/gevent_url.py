import gevent
from urllib import request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

url = "http://www.baidu.com"
url1 = "http://www.ifeng.com"
url2 = "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2726102536,2091908784&fm=26&gp=0.jpg"

image_url2 = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552389426056&di=eda76bdc2254eb44c04819057e87599b&imgtype=jpg&src=http%3A%2F%2Fimg1.imgtn.bdimg.com%2Fit%2Fu%3D3068506516%2C540373130%26fm%3D214%26gp%3D0.jpg"
image_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552389398316&di=24510cbf368070ab36a73cdc4dfffb05&imgtype=0&src=http%3A%2F%2Fwww.cad.zju.edu.cn%2Fhome%2Fgfzhang%2Ftraining%2FMatting%2Fpeacock.png"

web_url = "http://gttnbss.hztbc.com/ctrls/main.php";


def downloadWebSite(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
        print('Data:%d url=%s' % (len(data), url))
        # print(data)


def download(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # print('Data:', data.decode('utf-8'))
        print('Data:%d url=%s' % (len(data), url))


# 以二进制格式打开一个文件只用于写入
def download_url(url, name):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)

        folder_name = "image"
        if os.path.exists(folder_name):
            print("exist")
            pass
        else:
            print("not exist")
            os.mkdir(folder_name)

        new_f = open(folder_name + "/" + name, "wb")
        new_f.write(data)
        new_f.close()

        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # print('Data:', data.decode('utf-8'))
        print('Data:%d url=%s' % (len(data), url))


def main():
    # gevent.joinall({
    #     gevent.spawn(download, url),
    #     gevent.spawn(download, url1),
    #     gevent.spawn(download, url2)
    # })

    gevent.joinall({
        # gevent.spawn(download_url, url2, "1.jpg"),
        # gevent.spawn(download_url, image_url2, "2.jpg"),
        # gevent.spawn(download_url, image_url, "3.jpg"),
        gevent.spawn(downloadWebSite, web_url)
    })
    pass


if __name__ == '__main__':
    main()
