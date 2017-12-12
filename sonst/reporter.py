import requests

bot_token = '492708955:AAHgKSBYl0cJSeuOPotyFzm7UhUHSIg0FIw'
chat_id = '51828069'
result = requests.post("https://api.telegram.org/bot{0}/sendMessage".format(bot_token),
data={"chat_id": chat_id, "text": text, "disable_web_page_preview": "true"})

def status_reporter(report_text, bot_token, chat_id):
    """Gives a status report to telegram bot"""
    result = requests.post("https://api.telegram.org/bot{0}/sendMessage".format(bot_token),
    data={"chat_id": chat_id, "text": report_text, "disable_web_page_preview": "true"})

status_reporter(report_text, bot_token=bot_token, chat_id=chat_id,)
