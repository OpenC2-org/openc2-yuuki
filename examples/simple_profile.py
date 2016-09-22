from yuuki.dispatch import action


@action(target="openc2:domain")
def deny(target, actuator, modifier):
    """
    Note: return values are sent as the response to an OpenC2 cmd
    """
    return "Blocking domain {}".format(target['URI'])


@action(target="openc2:domain")
def allow(target, actuator, modifier):
    """
    Docstring for each openc2 action is used for QUERY openc2:openc2
    """
    return "Allowing domain {}".format(target['URI'])


@action(target="openc2:user")
def deny(target, actuator, modifier):
    """Each instance of the multimethod can have a unique docstring"""
    return "Denying user {}".format(target['name'])


@action(target="openc2:user")
def allow(target, actuator, modifier):
    return "Allowing user {}".format(target['name'])


@action(target="openc2:file", actuator="openc2:chmod")
def mitigate(target, actuator, modifier):
    return "Mitigating file with chmod"


@action(target="openc2:file", actuator="openc2:rm")
def mitigate(target, actuator, modifier):
    return "Mitigating file by deleting it"


def foo():
    return "I am not an OpenC2 action"

