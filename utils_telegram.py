# Imports
import config
import requests
from datetime import datetime


def telegram_bot_send_text(text: str):
    """
    Use telegram bot to send text to a chat.

    :param str text: text to send to the chat
    :return: Response, response object
    """
    # Log
    print('{} Sending text to phone'.format(datetime.today()))

    # Define request
    request = 'https://api.telegram.org/bot' + config.TOKEN + '/sendMessage?chat_id=' + config.CHAT_ID + '&parse_mode=Markdown&text=' + text

    # Send request
    response = requests.post(request)

    return response


def telegram_bot_send_photo(filepath: str):
    """
    Use telegram bot to send photo to a chat.

    :param str filepath: filepath of the photo to send to the chat
    :return: Response, response object
    """
    # Log
    print('{} Sending {} to phone'.format(datetime.today(), filepath))

    # Define request
    request = 'https://api.telegram.org/bot' + config.TOKEN + '/sendPhoto?chat_id=' + config.CHAT_ID

    # Send request
    response = requests.post(request, files={'photo': open(filepath, 'rb')})

    return response
