#!/usr/bin/env python2
# -*-: coding utf-8 -*-


class Skill(object):
    pass


def tvoff(hermes, intent_message):
    with open('/tmp/tvoff3', 'w') as fp:
        fp.close()
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))


if __name__ == "__main__":
    skill = Skill()
    
    with open('/tmp/tvoff1', 'w') as fp:
        fp.close()
    
    lang = "EN"
    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        with open('/tmp/tvoff2', 'w') as fp:
            fp.close()
        h.skill = skill
        h.subscribe_intent("tvoff", tvoff)
        h.loop_forever()