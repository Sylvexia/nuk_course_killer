import requests
from PIL import Image
from bs4 import BeautifulSoup
from itertools import islice
import lxml
import schedule
import time

acnt = input('input your account: ')
pswd = input('input your password: ')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    }
account = {
    'Account': acnt,
    'Password': pswd
}
prgid = {'Prgid':'CO0200'}

base_pix = [                                               #pixel 42,47
    [0, 255, 0, 0, 255],
    [255, 255, 0, 255, 255],
    [255, 255, 255, 255, 0],
    [255, 255, 0, 0, 255],
    [0, 255, 255, 0, 255],
    [0, 0, 255, 255, 255],
    [0, 255, 0, 0, 0],
    [255, 255, 255, 0, 255],
    [255, 0, 0, 0, 0],
    [0, 255, 255, 255, 0]
    ]



def login():

    crop_image = []
    pix_arr = []
    verify = ""
    a=0

    rs = requests.session()
    rs.post("https://course.nuk.edu.tw/Sel/SelectMain1.asp", data = account, headers=headers)
    rs.get('https://course.nuk.edu.tw/Sel/SelectMain.asp')
    rs.post("https://course.nuk.edu.tw/Sel/Main0195.asp",data = prgid)
    res=rs.get('https://course.nuk.edu.tw/Sel/Head0195.ASP')

    with open('certify.jpg','wb') as f:
        res =  rs.get('https://course.nuk.edu.tw/Sel/Certify_Image.asp', verify = False)
        f.write(res.content)

    image = Image.open('certify.jpg')
    image = image.convert('L')
    image = image.point(lambda x: 0 if x < 230 else 255, '1')

    for  i  in range(4):
        crop_image.append(image.crop((a,0,a+10,10)))
        a+=10
        pix_arr.append([pixel for pixel in islice(iter(crop_image[i].getdata()),42,47)])
        for j in range(10):
            if(list(pix_arr[i])==base_pix[j]):
                verify=verify+str(j)
    print(list(pix_arr))
    print(verify)
    #image.show()


    payload = {
        'total_count': 1,
        'Beg_Time': '',
        'Certify': verify,
        'agree': 'agree',
        'Cono1': 'CSB051',
        'Coname1': '電腦網路',
        'LKind1': '2',
        'Yclass1': 'A11055',
        'TWeek1': '2,2,2',
        'TCard1': '2,3,4',
        'Num1': '3',
        'Notup1': 'False',
        'Limit1': 'False',
        'Limit21': 1,
        'Cono2': '',
        'Coname2': '',
        'LKind2': 1,
        'Yclass2': '',
        'TWeek2': '',
        'TCard2': '',
        'Num2': '',
        'Notup2': '',
        'Limit2': '',
        'Limit22':'' ,
        'Cono3': '',
        'Coname3': '',
        'LKind3': 1,
        'Yclass3':'',
        'TWeek3': '',
        'TCard3': '',
        'Num3':'' ,
        'Notup3': '',
        'Limit3':'' ,
        'Limit23': ''
    }

    res  = rs.post('https://course.nuk.edu.tw/Sel/AddScript.asp',data= payload)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text,"lxml")
    print("log:")
    print(soup.prettify())
    print(soup.get_text())

schedule.every().day.at("12:29:53").do(login)
schedule.every().day.at("12:29:54").do(login)
schedule.every().day.at("12:29:55").do(login)
schedule.every().day.at("12:29:56").do(login)
schedule.every().day.at("12:29:57").do(login)
schedule.every().day.at("12:29:58").do(login)
schedule.every().day.at("12:29:59").do(login)
schedule.every().day.at("12:30:00").do(login)
schedule.every().day.at("12:30:01").do(login)
schedule.every().day.at("12:30:02").do(login)
schedule.every().day.at("12:30:03").do(login)  
schedule.every().day.at("12:30:04").do(login)
schedule.every().day.at("12:30:05").do(login)
schedule.every().day.at("12:30:06").do(login)
schedule.every().day.at("12:30:07").do(login)
schedule.every().day.at("12:30:08").do(login)

login()
while True:
    schedule.run_pending()
    time.sleep(0.5)