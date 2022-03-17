from distutils import file_util
import re
import requests
import os
#request for the website
res = requests.get('https://www.pixiv.net/ranking.php')
if res.status_code == 200:
    info = re.findall(r"/artworks/\d+", res.text)
    info = info[::2]
    count = 0  

    #find date
    date = re.findall(r"\[\w+\.\w+\.\w+\]", res.text)
    date = date[0]
    date = date.strip("[").strip("]")
    print(date)
    os.makedirs("./data/"+date, exist_ok=True)
    pickpath = './data/'+date

    #find names
    name = re.findall(r"\"noopener\">.*?</a>", res.text)
    name = name[1:51]
    for i in range(0, len(name)):
        name[i] = name[i].strip('"noopener">').strip('</a>')
        name[i] = name[i].replace('/','.').replace('\\','.').replace('*','.').replace(':','.').replace('?','.').replace('"','.').replace('<','.').replace('>','.').replace('|','.')        
        print(name)
    #download the images
    for something in info:
        req = requests.get('https://www.pixiv.net' + something)
        if req.status_code == 200:
            u = re.findall(r"https://i\.pximg\.net/img-original/img/.*?g", req.text)
            print(u[0])
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',            
                        'referer':'http://www.pixiv.net%s' % str(something)}  
            try: 
                filename = pickpath+"/" + str(name[count]) + ".jpg"
                r = requests.get(u[0], headers=headers)
                with open(filename, 'wb') as f:
                    f.write(r.content)
                    f.close()
                print('this is ' + str(count) + 'st img')
            except:
                print('failure')   
        else:
            print("failed connecting to https://www.pixiv.net" + something)
        count += 1
else:
    print("failed connecting to https://www.pixiv.net/ranking.php")



