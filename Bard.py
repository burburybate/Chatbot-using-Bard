#This Code Snippet is used to connect to Google Bard Service and Create a new chat instance.
from Pythonguii import get_auth_info
PSID, PSIDCC, PSIDTS = get_auth_info() 
from Pythonguii import bard_ui

def bard_connect():
    import requests
    from bardapi import Bard, SESSION_HEADERS
    session = requests.Session()
    session.headers = SESSION_HEADERS
    token = PSID
    session.cookies.set("__Secure-1PSID", PSID)
    session.cookies.set( "__Secure-1PSIDCC", PSIDCC)
    session.cookies.set("__Secure-1PSIDTS", PSIDTS)
    bard = Bard(token=token, session=session)
    return bard

bard = bard_connect()
chat_window = bard_ui(bard)
chat_window.mainloop()