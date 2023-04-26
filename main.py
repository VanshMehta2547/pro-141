from flask import Flask, jsonify
import csv
all_articles = []
liked_articles = []
unliked_articles = []
with open('articles.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)
@app.route('/get-article')
def get_article():
    return jsonify({"article":all_articles[0], "status":"success"}), 200

@app.route('/liked-article', methods = ["POST"])
def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({"status":"success"})

@app.route('/unliked-article', methods = ["POST"])
def unliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({"status":"success"})

if(__name__=="__main__"):
    app.run()