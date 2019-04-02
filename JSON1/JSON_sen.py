import socket
import cv2
import numpy
import json


HOST = "127.0.0.1"
PORT = 50000
global s


def main():
    global s
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    

    s.connect((HOST,PORT))

    name=input("請輸入欲傳送之圖片名稱(注意！需與本程式位於同一資料夾)：")
    try:
        img=cv2.imread(name)
    except:
        print("圖片擷取失敗")
    dir=input("請輸入欲儲存地點(注意!斜線需要兩畫如：C:\\User)：")
    name_dir=dir+"\\"+name
    im_list=img.tolist()
    img_json=json.dumps(im_list)
    s.send(str.encode("name_d"))
    s.send(str.encode(name_dir))
    temp=""
    n=0
    s.send(str.encode("start"))
    while True:
        temp=temp+img_json[n:n+1:]
        if len(temp)==1024:
            s.send(str.encode(temp))
            temp=""
        elif len(img_json)==n+1:
            s.send(str.encode(temp))
            print("end\n")
            break
        n+=1
    

if __name__=="__main__":
    main()