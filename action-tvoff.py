#!/usr/bin/env python2
# -*-: coding utf-8 -*-


class Skill(object):
    pass


def tvoff(hermes, intent_message):
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))


if __name__ == "__main__":
    skill = Skill()
    
    lang = "EN"
    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.skill = skill
        h.subscribe_intent("hermes/intent/jiffe:tvoff", tvoff)
        h.loop_forever()