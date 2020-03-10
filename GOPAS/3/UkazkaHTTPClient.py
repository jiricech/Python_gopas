# Nacteni stranky z webu

import urllib.request

try:
    html = urllib.request.urlopen("https://www.google.com").read()
    print(html)
except:
    print("Ejhle chybka!")
