import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def fibbonaci():
    next = 1
    preview = 0
    limit = 50
    found = 0
    answer = "0, "
    while (found < limit):
        tmp = next
        next = next + preview
        preview = tmp
        found=found+1
        answer+= str(next) + ", "
        if(found == 20 or found == 34 or found == 47):
            answer+= str(next) + "\n"

    return answer

if __name__ == "__main__":
    port = int (os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)