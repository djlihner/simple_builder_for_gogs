from flask import Flask, request, abort
from json import loads
from builder import builder

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    try:
        payload = loads(request.data)
        clone_url = payload['repository']['clone_url']
        branch_name = (payload['ref']).split("/")[2]

        builder.clean_project()
        builder.clone_project(clone_url, branch_name)
        builder.code_analysis()
    except ConnectionError:
        abort(400)
    return "Ok!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
