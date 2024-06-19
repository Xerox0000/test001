from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/proxy')
def proxy():
    # プロキシの処理をここに書く
    return jsonify({"status": "プロキシが正常に動作しています"}), 200

if __name__ == '__main__':
    app.run(debug=True)
