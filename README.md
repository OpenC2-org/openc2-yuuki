# openc2-yuuki

> "My family name is Yugano. My given name is Yuuki. I have no redeeming qualities.
> ...
> This is because the Internet has ruined my way of looking at the world."
> - from A Girl Corrupted by the Internet is the Summoned Hero?! by Eliezer Yudkowsky

Yuuki is a Python package for building an OpenC2 proxy.

## Usage

Create a python virtual environment and pip install yuuki. (Yuuki is alpha software; installing globally is not recommended.)

Start a proxy:

    python -m yuuki.proxy simple_profile.py

Start a debug shell:

    python -m yuuki.shell http://localhost:9001

The general form of a command issued from the debug shell:

    openc2> ACTION target:type {some: specifier, another: specifier} actuator:type {some: specifier} some: modifier, another: modifier

Actuators and modifiers are optional.

Examples supported by simple_profile.py

    openc2> DENY openc2:domain {URI: evil.com}
    openc2> DENY openc2:user {name: John}
    openc2> MITIGATE openc2:file {} openc2:rm {}

