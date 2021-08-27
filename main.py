from flask import Flask, json,jsonify,request
import csv

all_article=[]

with open("article.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_article=data[1:]

like=[]
didnotlike=[]


app=Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_article[0], 
        "status":"success"
    })

@app.route("/liked-article",methods=["POST"])
def liked_article():
    article=all_article[0]
    all_article=all_article[1:]
    like.append(article)
    return jsonify({
        "status":"success"
    }),201
    
@app.route("/did-not-like-article",methods=["POST"])
def did_not_like_article():
    article=all_article[0]
    all_articles=all_article[1:]
    didnotlike.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()
