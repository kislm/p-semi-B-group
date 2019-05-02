from flask import Flask,render_template
import base

#appにFlaskを定義して使えるようにする
app = Flask(__name__)

@app.route('/index/')
def locate():
    lat = base.dict.get("lat")
    lng = base.dict.get("lng")
    radius = base.dict.get("radius")
    return render_template('index.html', lat=lat,lng=lng,radius=radius)


if __name__ == "__main__":
    app.run()
