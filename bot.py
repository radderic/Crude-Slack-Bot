from slackclient import SlackClient
from time import sleep
from pprint import pprint

tokenFile = open('token.txt', 'r')
token = tokenFile.read().rstrip()
slack_client = SlackClient(token)
identifier = '!'

def echo(text, where):
    sendMessage(text, where)

def sendMessage(text, channel):
    slack_client.api_call(
    'chat.postMessage',
    channel=channel,
    text=text
    )

def handleMessage(text, where, who):
    #arbitrary text
    if(text == 'hi'):
        sendMessage('hi', where)
    #calls bot directly
    if(text.startswith(identifier)):
        command = text.split(' ')[0][1:]
        text = text.split(' ', 1)[1]
        if(command == 'echo'):
            echo(text, where)

def handleEvent(event):
    if(event[0]['type'] == 'message'):
        text = event[0]['text']
        where = event[0]['channel']
            handleMessage(text, where)

if __name__ == "__main__":
    print('Attempting to connect...')
    if(slack_client.rtm_connect()):
        print('Connection successful!')
        while True:
            event = slack_client.rtm_read()
            if(len(event) != 0):
                print(event)
                handleEvent(event)
            sleep(1)
    else:
        print("Failed to connect")


