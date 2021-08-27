from flask import Flask, render_template
from post import Post
import requests
import os

data_url = os.getenv("posts_url")

response = requests.get(url=data_url)
articles_data = response.json()

posts = [Post(post_id=article["id"],
              post_title=article["title"],
              post_subtitle=article["subtitle"],
              post_body=article["body"]
              ) for article in articles_data]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=posts)


@app.route("/post/<int:index>")
def get_post(index):
    selected_post = None
    for blog_post in posts:
        if blog_post.id == index:
            selected_post = blog_post
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
