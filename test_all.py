from bs4 import BeautifulSoup

import urllib.request

import urllib3

import time

header ={
'Cookie':'pgv_pvi=1551156944; eas_sid=I1U5V1o4C1Z9R2C2Q82045j1s2; pgv_pvid=57089460; RK=W8dCNAIvMz; ptcz=e0f373902bbf91f6898897dc5ff456b70884941dd4332f591ee2c8d919e858ed; LW_uid=p16511N5L7c296x5J4z6x1F0j6; ptui_loginuin=1803514733; o_cookie=451735634; tvfe_boss_uuid=c659b78a82ccc57e; pt2gguin=o0451735634; ue_uk=f118ffdd56465ffb289dda7a67809670; ue_uid=0d3224e5ac77fc0c327effe753a834c5; LOL_API_W2013_USER_451735634Area=3; ue_ts=1521445112; ue_skey=d24c08dc668e898d4a5e1eff28ff2f7e; LW_pid=1d6b8497ab034dff10325b2dbc84328d; rewardsn=; wxtokenkey=777',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

http = urllib3.PoolManager()

def save_text(times,url):
    r = http.request('GET', url, headers = header)
    
    resp = BeautifulSoup(r.data, "html5lib")
    title = resp.find('h2',id="activity-name")
    date_author = resp.find_all('em',class_="rich_media_meta rich_media_meta_text")
    poster = resp.find('a',id="post-user")
    content = resp.find('div',id="js_content").get_text()
    
    savefile_name = 'newtext\\35\\' + str(times)+ '+'
    for tmp in date_author:
        savefile_name = savefile_name + tmp.string + '+'
    #savefile_name = savefile_name + date_author[0].string + '+'
    savefile_name = savefile_name + poster.string +".txt"
    if (savefile_name.find('/') != -1 or savefile_name.find('\t') != -1):
        savefile_name = 'newtext\\35\\' + str(times)+ '+' + date_author[0].string + '+' + poster.string +".txt"
    
    fh = open(savefile_name,'w',encoding='utf-8')
    print(title.string, file = fh)
    for tmp in date_author:
        print(tmp.string, file = fh)
    print(poster.string, file = fh)
    print(content,file = fh)
    fh.close()

inputfile = open('35.txt','r')
count = 0
for line in inputfile:
    count = count + 1
    if (count < 690):
        continue
    try:
        save_text(count, line)
    except AttributeError as e:
            print (str(count) + "type error")
            continue
    if (count % 50 == 0):
        time.sleep(5)
