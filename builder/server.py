from builder import env_builder

from json import loads
from flask import Flask, request, abort


app = Flask(__name__)


@app.route("/", methods=['GET'])
def main_screen():
    return "Hello!"


@app.route("/builder_event", methods=['POST'])
def deploying_build():
    try:
        payload = loads(request.data)

        git_repository_url = payload['repository']['clone_url']
        repository_branch_name = (payload['ref']).split("/")[2]

        env_builder.deploying_build(git_repository_url, repository_branch_name)
    except ConnectionError:
        abort(400)
    return "Build Complete!"


def run():
    app.run(port=4567, debug=True)
