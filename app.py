from flask import Flask, render_template, request, redirect, jsonify
import pyshorteners

app = Flask(__name__)
s = pyshorteners.Shortener()


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        response = request.form
        short = s.tinyurl.short(response['url'])
        return render_template('home.html', url=response, shortened_url=short)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


