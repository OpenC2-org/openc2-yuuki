#!/usr/bin/env python

import argparse
import os

from flask import Flask, jsonify, request, abort
from dispatch import Dispatcher
from ConfigParser import SafeConfigParser

app = Flask(__name__)

PROFILE = None

@app.route('/')
def ok():
    """
    Verify the system is running.
    """
    return jsonify({"response": "200 OK"}), 200


@app.errorhandler(400)
def bad_request(e):
    """
    Respond to a malformed OpenC2 command.
    """
    return jsonify({"response": "400 Bad Request"}), 400


@app.errorhandler(500)
def internal_server_error(e):
    """
    Uncaught proxy error
    """
    return jsonify({"response": "500 Internal Server Error"}), 500


@app.route('/', methods=['POST'])
def recieve():
    """
    Recieve an OpenC2 command, process and return response.

    All OpenC2 commands should be application/json over HTTP POST
    """
    if not request.json:
        abort(400)

    response = PROFILE.dispatch(request.get_json())
    return jsonify(response), 200

def parse_config(config_file):

    """
    Receive a file path and parse it to a dict
    """

    config_reader = SafeConfigParser()
    config_reader.read(config_file)
    config_dict = {}

    for section_name in config_reader.sections():

        config_dict[section_name] = {}

        for name, value in config_reader.items(section_name):

            config_dict[section_name][name] = value
    
    return config_dict

def main():

    """
    Parse configuration and start flask app.
    """
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--conf', type=str, default="yuuki.conf",help="Location of yuuki.conf")

    args = parser.parse_args()

    if os.path.isfile(args.conf):

        app.config["yuuki"] = parse_config(args.conf)

    else:

        # Let me know how you want to handle exceptions
        raise(Exception("Config file not found")) 

    # Load profiles
    profile_list = []
    for profile in app.config["yuuki"]["profiles"]:

        # TODO - Add better logging
        print " * Loading profile %s" % profile
        profile_list.append(app.config["yuuki"]["profiles"][profile])
        
    # Make dispatcher with loaded modules    
    global PROFILE 
    PROFILE = Dispatcher(profile_list)

    # Run the app    
    app.run(port=int(app.config["yuuki"]["server"]["port"]),host=app.config["yuuki"]["server"]["host"])


if __name__ == "__main__":

    main()

