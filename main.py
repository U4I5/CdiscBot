# Importation module(s)
# Module Content our credentials 
from . import credentials_login
import httpx as bot

# Settings
# Cdiscount home page
homeurl = "https://www.cdiscount.com/"
# Cdiscount Authentification url
athurl =  'https://order.cdiscount.com/Account/LoginLight.html'

# Headers of Requests
headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
# Data form use to log in 
payload =   {'CustomerLogin.CustomerLoginFormData.Email' :	credentials_login.username,
            'CustomerLogin.CustomerLoginFormData.Password' : credentials_login.password}
#User function 
def user(): 
    with bot.Client() as s:
        # Get cookie Firstly
        s.get(homeurl)
        # Data We need to log in
        s.post(athurl, headers=headers, data=payload, timeout=None )
        # basketurl content oder's
        basketurl = ("https://www.cdiscount.com/Basket.html")
     res = s.get(basketurl)

    print(res.txt)