# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

__author__ = 'Galleani'

from celery.task import task
from celery.utils.log import get_task_logger
from core.constants import TOKEN_SLACK_API, TEAM_CHANNEL

__author__ = 'Rafael'
from slacker import Slacker

logger = get_task_logger(__name__)

@task
def alarm():
    import random
    logger.info('Iniciando Alarme')
    number = random.randint(80, 120)
    if number > 100:
        msg = "%s requisições. Crítico!"%number
        slack = Slacker(TOKEN_SLACK_API)
        slack.chat.post_message('#'+TEAM_CHANNEL, msg)
    else:
        msg = "%s requisições."%number
    logger.info(msg)

