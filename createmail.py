import random
import string
import requests
import json

def generate_mail():
    letters = string.ascii_lowercase
    name=''.join(random.choice(letters) for i in range(12))
    domains = ['chitthi.in', 'tofeat.com', 'intopwa.com', 'inpwa.com', 'rover.info', 'fexpost.org', 'mailto.plus','mailbox.in.ua', 'fexpost.com']
    mailname=random.choice(domains)
    return name+"@"+mailname
def mail_inbox(mailadress):
    url="https://tempmail.plus/api/mails?email="+str(mailadress)+"&limit=20&epin="
    response = requests.get(url)
    return json.loads(response.text)

mail=generate_mail()
mail_icerik=mail_inbox(mail)["mail_list"]
