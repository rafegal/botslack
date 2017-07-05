__author__ = 'Galleani'
import django
django.setup()

from slacker import Slacker

from time import sleep
from core.models import Interaction
from core.constants import TOKEN_SLACK_API, TEAM_CHANNEL

def beat():
    slack = Slacker(TOKEN_SLACK_API)
    channel_id = slack.channels.get_channel_id(TEAM_CHANNEL)
    print channel_id
    list = []
    while True:
        sleep(2)
        info =  slack.channels.info(channel_id).body
        try:
            text = info['channel']['latest']['text']
            user = info['channel']['latest']['user']
            ts =  info['channel']['latest']['ts']
            if ts not in list:
                list.append(ts)
                new = text.split(' ')
                input = new[0]
                parm = new[1]
                interaction = Interaction.objects.get(input=input)
                status, binds = interaction.execute(parm)
                if status == 1:
                    output = interaction.get_output(binds)
                    slack.chat.post_message('#'+TEAM_CHANNEL, output)
            list.append(ts)
        except Exception as ex:
            pass

if __name__ == '__main__':
    beat()
    # text = '!cep 14802120'
    # new = text.split(' ')
    # input = new[0]
    # parm = new[1]
    # print input, parm
    # interaction = Interaction.objects.first()
    # status, msg = interaction.execute(parm)
    # print status, msg
