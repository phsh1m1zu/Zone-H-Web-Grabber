#Modified by Pr1nd3x
#Code Upgraded by CHATGPT
import urllib.request
import re
import time
import socket

def collector(pageUrl, defacer, num):
    target = pageUrl
    try:
        req = urllib.request.Request(
            target,
            headers={'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
        )
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
        l = re.findall('red on [\w.]+ [\w.]+ [\w.]+', data)
        l = l[0].split(' ')
        date = l[2] + ' ' + l[3] + ' ' + l[4]
        print('Google Cache Date:', date)
        domains = re.findall('<td>[\w.-]+', data)
        for i in domains:
            if '.' in i:
                i = i.replace('<td>', '')
                print('[{}] http://{}'.format(num, i))
                num += 1
                with open('zh archive {}.txt'.format(defacer), 'a+') as file:
                    file.write('http://{}\n'.format(i))
        return num
    except Exception as e:
        print('Uh oh! An error occurred. I assume that it\'s your internet connection that caused this problem!')
        print('Still skipping, let\'s see if anything we find on the next!')
        print('Error:', str(e))
        return num

def main():
    num = 1
    print('Zone-H Archive Scanner')
    print('Modified by Pr1nd3x')
    defacer = input("Enter Notifier Name: ")
    if not defacer:
        print('Are you playing with me? Type in a name!')
        exit(0)
    print('Notifier Under Observation:', defacer)
    print('Collecting from page: [1]')
    num = collector("http://webcache.googleusercontent.com/search?q=cache:www.zone-h.org/archive/notifier%3D" + defacer + "&num=1&client=opera&hl=en&gl=bd&strip=0&vwsrc=1", defacer, num)
    # time.sleep(2)
    for i in range(2, 51):
        print('Collecting from page: [{}]'.format(i))
        num = collector("http://webcache.googleusercontent.com/search?q=cache:www.zone-h.org/archive/notifier%3D" + defacer + "/page=" + str(i) + "&num=1&client=opera&hl=en&gl=bd&strip=0&vwsrc=1", defacer, num)
        # time.sleep(2)
    print('Total collected domains:', num)
    print('Data is also stored on ', 'zh archive {}.txt'.format(defacer))

main()
