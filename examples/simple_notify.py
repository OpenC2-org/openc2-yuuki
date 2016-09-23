from subprocess import call
from yuuki.dispatch import action

CARRIERS = {"AT&T": "txt.att.net",
            "T-Mobile": "tmomail.net",
            "Verizon": "vtext.com",
            "Sprint": "pm.sprint.com",
            "Virgin Mobile": "vmobl.com",
            "Tracfone": "mmst5.tracfone.com",
            "Metro PCS": "mymetropcs.com",
            "Boost Mobile": "myboostmobile.com",
            "Cricket": "sms.mycricket.com",
            "Ptel": "ptel.com",
            "Republic Wireless": "text.republicwireless.com",
            "Suncom": "tms.suncom.com",
            "Ting": "message.ting.com",
            "U.S. Cellular": "email.uscc.net",
            "Consumer Cellular": "cingularme.com",
            "C-Spire": "cspire1.com",
            "Page Plus": "vtext.com"}


@action(target='openc2:cellphone')
def notify(target, actuator, modifier):
    """
    Send an alert to a cellphone.
    
    Required target specifiers:
    cellphone number - target['number']
    cell carrier - target['carrier']
    alert message - target['message']
    """
    to = "{}@{}".format(target['number'], CARRIERS[target['carrier']])
    subject = "OpenC2 Alert"
    message = target['message']
    mailcmd = "echo '{}' | mail -s '{}' {}".format(message, subject, to)

    return call(mailcmd, shell=True)


@action(target='openc2:domain')
def mitigate(target, actuator, modifier):
    """Some documentation about mitigation"""
    return "I can't do that, Dave"


