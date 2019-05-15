from flask import Flask,render_template
import base

#appにFlaskを定義して使えるようにする
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/home/')
def locate():
    lat = base.dict.get("lat")
    lng = base.dict.get("lng")
    radius = base.dict.get("radius")
    link = "https://www.google.com/maps/@" + lat + "," + lng + ",16z"
    return render_template('home.html', lat=lat,lng=lng,radius=radius,link=link)


if __name__ == "__main__":
    app.run()
