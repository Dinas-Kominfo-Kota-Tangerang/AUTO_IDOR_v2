import requests
import json
from bs4 import BeautifulSoup
from IPython.utils import text


__author__ = 'N Auliajati - Dinas Kominfo Kota Tangerang'

kies = {'ci_session': 'AAABBBCCCDDD'}

while True:
    kue = {"cookie": kies}
    payload = {
  'id': '1234567890',
  'pass_lama': 'AAA',
  'pass_baru': 'BBB',
  'konfirmasi_pass': 'CCC'
}
    for i in range(1):
        r = requests.post("https://redacted.com/site/change_password/", data=json.dumps(payload))
        if len(r.content) > 0:
            html_file = BeautifulSoup(r.text, "html.parser")
            print(r.status_code, html_file.prettify(), file=open("oo.html", "f"))
    break