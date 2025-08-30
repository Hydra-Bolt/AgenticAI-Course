from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import run_agent, get_version

app = Flask(__name__)
CORS(app)

@app.route('/api/agent', methods=['POST'])
def api_agent():
    data = request.get_json(force=True, silent=True) or {}
    task = data.get("task", "general")
    user_input = data.get("input", "")
    result = run_agent(task, user_input)
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8000, debug=True)