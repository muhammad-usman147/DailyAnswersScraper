from flask import Flask,jsonify,render_template
import pandas as pd
import os
import re
app = Flask(__name__)

@app.route('/')
def Home():
    Q = pd.read_csv("ScrapedQuestions.csv")
    A = pd.read_csv("ScrapedAnswer.csv")
    query  = {}
    Qx = Q.iloc[1,:]
    Ax = A.iloc[1,:]
    query['desc'] = re.sub('<[^<]+?>', '', Qx.description)
    query['featured_image_url'] = Qx.featured_image_url
    query['post_data'] = Qx.post_data
    query['post_url'] = Qx.post_url
    query['title'] = Qx.title
    query['body_image_url'] = Ax.body_image_url
    return render_template('question.html',query=query)
@app.route("/Answer")
def CheckAnswer():
    query = {}
    A = pd.read_csv("ScrapedAnswer.csv")
    Ax = A.iloc[1,:]
    query['desc'] = re.sub('<[^<]+?>', '', Ax.description)
    query['featured_image_url'] = Ax.featured_image_url
    query['post_data'] = Ax.post_data
    query['post_url'] = Ax.post_url
    query['title'] = Ax.title
    query['body_image_url'] = Ax.body_image_url
    query['answer'] = Ax.answer
    return render_template('answers.html',query=query)
if __name__ == '__main__':
    app.run(debug=True)
