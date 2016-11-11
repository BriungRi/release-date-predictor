from flask import Flask, request
import index
app = Flask(__name__)

@app.route('/api/release_date')
def main():
    item = request.args.get('item')
    return index.get_release_date(item)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
