from flask import Flask
from imdbpie import Imdb

app = Flask(__name__)
@app.route('/api1', methods=['GET'])
def api1():
    imdb = Imdb()
    imdb = Imdb(anonymize=True)
    var1 = imdb.top_250()
    var2 = imdb.search_for_title("FightClub")
    print(var1)
    print(var2)
    return var1
    return var2
@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"
    

if __name__ == '__main__':
    app.run(debug=True)