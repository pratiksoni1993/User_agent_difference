import sys
url = sys.argv[1]
from diff_directories import diff_directories
command = "wget -t 7 -w 5 --random-wait --limit-rate=1024K -e robots=off -H -p -k -U "
user_agent_list = [\
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",\
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",\
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",\
"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",\
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:35.0) Gecko/20100101 Firefox/35.0",\
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",\
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",\
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",\
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91",\
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36 OPR/18.0.1284.49",\
"Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.16",\
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.71 (KHTML like Gecko) WebVideo/1.0.1.10 Version/7.0 Safari/537.71",\
"Mozilla/5.0 (Windows; U; Windows NT 6.2; es-US ) AppleWebKit/540.0 (KHTML like Gecko) Version/6.0 Safari/8900.00",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",\
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",\
"Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00",\
"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.1 (KHTML like Gecko) Version/7.0.6 Safari/537.78.1" ,\
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML like Gecko) Version/6.0.2 Safari/536.26.17",\
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.166 Safari/537.36 OPR/20.0.1396.73172",\
"Opera/9.80 (X11; Linux i686) Presto/2.12.388 Version/12.16",\
"Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",\
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",\
"Mozilla/5.0 (X11; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0",\
"Mozilla/5.0 (X11; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0",\
"Mozilla/5.0 (X11; CrOS x86_64 5841.83.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.138 Safari/537.36",\
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1478.0 Safari/537.36",\
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.56 Safari/537.4",\
"Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-T537A Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.141 Safari/537.36",\
"Mozilla/5.0 (Linux; U; Android 4.3; en-us; sdk Build/MR1) AppleWebKit/536.23 (KHTML, like Gecko) Version/4.3 Mobile",\
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3 Safari/536.23",\
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190",\
"Opera/9.80 (Android; Opera Mini/7.5.33361/31.1543; U; en) Presto/2.8.119 Version/11.1010",\
"Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30",\
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us ; LS670 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1/UCBrowser/8.6.1.262/145/355",\
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7) UCBrowser/2.9.0.263"\
       ]

import os
base_dir = os.getcwd()
for i in range(len(user_agent_list)):
        os.makedirs(str(i))
        os.chdir(str(i))
        os.system(command + "'"+user_agent_list[i] + "' " + url)
        os.chdir(base_dir)
        
