import requests
from yuuki.dispatch import action

# Static Entry Pusher has been renamed in the Floodlight API
# 'staticentrypusher' on master
# 'staticflowpusher' v1.0 - v1.2
# 'staticflowentrypusher' v0.91
MODULE = 'staticentrypusher'

# Floodlight controller IP
CONTROLLER_IP = 'localhost'

# Floodlight REST API port (default 8080)
PORT = 8080


@action(target='sdn:flow')
def set(target, actuator, modifier):
    """
    Add/set a static flow; requires target specifier 'entry'.

    The entry is a json object specifying a flow as described in the
    Floodlight documentation. See:
    https://floodlight.atlassian.net/wiki/display/floodlightcontroller/

    Example invocation:
    SET sdn:flow {"entry": {"switch": "00:00:00:00:00:00:00:01", "name": ...}}
    """
    uri = 'http://{}:{}/wm/{}/json'.format(CONTROLLER_IP, PORT, MODULE)
    r = requests.post(uri, json=target['entry'])

    return r.status_code


@action(target='sdn:flow')
def delete(target, actuator, modifier):
    """
    Delete a static flow entry by name; requires target specifier 'entry'.

    Example invocation:
    DELETE sdn:flow {"entry": {"name": "flow-mod-1"}}
    """
    uri = 'http://{}:{}/wm/{}/json'.format(CONTROLLER_IP, PORT, MODULE)
    r = requests.delete(uri, json=target['entry'])

    return r.status_code


@action(target='sdn:flow')
def query(target, actuator, modifier):
    """
    Get all static flow entries on target["switch"]

    Example invocations:
    QUERY sdn:flow {"switch": "00:00:00:00:00:00:00:01"}
    QUERY sdn:flow {"switch": "all"}
    """
    uri = 'http://{}:{}/wm/{}/list/{}/json'.format(
            CONTROLLER_IP, PORT, MODULE, target["switch"])
    r = requests.get(uri)

    return r.json()


@action(target='sdn:switch')
def query(target, actuator, modifier):
    """
    Get a summary of all switches.

    Example invocation:
    QUERY sdn:controller {}
    """
    uri = 'http://{}:{}/wm/core/controller/switches/json'.format(
            CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


# Controller statistics

@action(target='sdn:controller.memory')
def query(target, actuator, modifier):
    """
    Get controller memory usage

    Example invocation:
    QUERY sdn:controller.memory {}
    """
    uri = 'http://{}:{}/wm/core/memory/json'.format(CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


@action(target='sdn:controller.health')
def query(target, actuator, modifier):
    """
    Get controller health

    Example invocation:
    QUERY sdn:controller.health {}
    """
    uri = 'http://{}:{}/wm/core/health/json'.format(CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


@action(target='sdn:controller.version')
def query(target, actuator, modifier):
    """
    Get controller version

    Example invocation:
    QUERY sdn:controller.version {}
    """
    uri = 'http://{}:{}/wm/core/memory/json'.format(CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


@action(target='sdn:controller.uptime')
def query(target, actuator, modifier):
    """
    Get controller uptime

    Example invocation:
    QUERY sdn:controller.uptime {}
    """
    uri = 'http://{}:{}/wm/core/system/uptime/json'.format(CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


# Firewall

@action(target="sdn:firewall")
def start(target, actuator, modifier):
    """
    Enable the firewall
    
    Example invocation:
    START sdn:firewall {}
    """
    uri = 'http://{}:{}/wm/firewall/module/enable/json'.format(
            CONTROLLER_IP, PORT)
    r = requests.put(uri, data="")

    return r.status_code


@action(target="sdn:firewall")
def stop(target, actuator, modifier):
    """
    Disable the firewall

    Example invocation:
    STOP sdn:firewall {}
    """
    uri = 'http://{}:{}/wm/firewall/module/disable/json'.format(
            CONTROLLER_IP, PORT)
    r = requests.put(uri, data="")
    
    return r.status_code


@action(target="sdn:firewall.status")
def query(target, actuator, modifier):
    """
    Get firewall status

    Example invocation:
    QUERY sdn:firewall.status
    """
    uri = 'http://{}:{}/wm/firewall/module/status/json'.format(
            CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


@action(target="sdn:firewall.rules")
def query(target, actuator, modifier):
    """
    Get firewall rules

    Example invocation:
    QUERY sdn:firewall.rules
    """
    uri = 'http://{}:{}/wm/firewall/rules/json'.format(CONTROLLER_IP, PORT)
    r = requests.get(uri)

    return r.json()


@action(target="sdn:firewall.rules")
def set(target, actuator, modifier):
    """
    Set a new firewall rule as defined by target["rule"]

    target["rule"] should be a json object as described in the
    Floodlight documenation. See:
    https://floodlight.atlassian.net/wiki/display/floodlightcontroller/

    Example invocation:
    SET sdn:firewall.rules {"rule": {"field": "value", ...}}
    """
    uri = 'http://{}:{}/wm/firewall/rules/json'.format(CONTROLLER_IP, PORT)
    r = requests.post(uri, json=target["rule"])
    
    return r.status_code


@action(target="sdn:firewall.rules")
def delete(target, actuator, modifier):
    """
    Delete a firewall rule as defined by target["ruleid"]

    Example invocation:
    DELETE sdn:firewall.rules {"ruleid": "<int>"}
    """
    uri = 'http://{}:{}/wm/firewall/rules/json'.format(CONTROLLER_IP, PORT)
    r = requests.delete(uri, json={"ruleid": target["ruleid"]})

    return r.status_code


