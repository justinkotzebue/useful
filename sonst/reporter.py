
# coding: utf-8

# In[14]:

import requests


# In[17]:

bot_token = '492708955:AAHgKSBYl0cJSeuOPotyFzm7UhUHSIg0FIw'
chat_id = '51828069'
text = 'testing bot'
result = requests.post("https://api.telegram.org/bot{0}/sendMessage".format(bot_token),
data={"chat_id": chat_id, "text": text, "disable_web_page_preview": "true"})


# In[18]:

def status_reporter(bot_token, chat_id, report_text):
    """Gives a status report to telegram bot"""
    result = requests.post("https://api.telegram.org/bot{0}/sendMessage".format(bot_token),
    data={"chat_id": chat_id, "text": text, "disable_web_page_preview": "true"})


# In[22]:

status_reporter(bot_token=bot_token, chat_id=chat_id, report_text=text)


# In[ ]:



