from slackclient import SlackClient
from time import sleep
from pprint import pprint

token = 'token goes here'
slack_client = SlackClient(token)
identifier = '!testbot'

def getSelfID():
    data = slack_client.api_call('users.list', token=TOKEN)
    for member in data['members']:
        if(member['name'] == 'test_bot'):
            print("id found", member['name'], member['id'])
            return member['id']
    return False

def fromSelf(who):
    if(getSelfID == who):
        return True
    else:
        return False

def sendMessage(text, channel):
    slack_client.api_call(
    'chat.postMessage',
    channel=channel,
    text=text
    )

def handleMessage(text, where, who):
    #arbitrary text
    if(fromSelf(who) == False):
        if(text == 'hi'):
            sendMessage('hi', where)
        #calls bot directly
        if(text.startswith(identifier)):
            print("I would do something here")

def handleEvent(event):
    if(event[0]['type'] == 'message'):
        text = event[0]['text']
        where = event[0]['channel']
        if(event[0].contains('user')):
            who = event[0]['user']
            handleMessage(text, where, who)


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


