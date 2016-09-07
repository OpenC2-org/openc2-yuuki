#!/usr/bin/env python

import argparse

from flask import Flask, jsonify, request, abort
from dispatch import Dispatcher

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


def main():
    """
    Parse configuration and start flask app.

    WARNING: only a single profile file is supported at this time
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9001,
                        help="port to listen on (default=9001)")
    parser.add_argument('profiles', nargs='+',
                        help="full path to OpenC2 profile")

    args = parser.parse_args()
    
    global PROFILE
    PROFILE = Dispatcher(*args.profiles)

    app.run(port=args.port)


if __name__ == "__main__":
    main()

