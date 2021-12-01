from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    username = request.form['username']
    file = open("white-list.txt", "a+")
    file.writelines(username)
    file.write("\n")
    file.close()
    return "You have been added to whitelist"

if __name__ == '__main__':
  app.run(debug=True)
