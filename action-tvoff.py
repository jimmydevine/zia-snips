#!/usr/bin/env python2
# -*-: coding utf-8 -*-
from hermes_python.hermes import Hermes
import hermes_python


MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Skill(object):
    pass


def tvoff(hermes, intent_message):
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, 'TV Off')


if __name__ == "__main__":
    skill = Skill()
    print 'TVOFF STARTED'
    
    lang = "EN"
    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.skill = skill
        h.subscribe_intent("jiffe:tvoff", tvoff)
        h.loop_forever()