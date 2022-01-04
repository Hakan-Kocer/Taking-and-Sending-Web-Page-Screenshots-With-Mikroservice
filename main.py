from flask import Flask, app
from moduls.url_to_screenshot_foto_to_base64 import screenshot_foto_to_base64

app=Flask(__name__)

@app.route('/<string:url>', methods=['GET'])
def find(url):
    img_base64=screenshot_foto_to_base64(url=url)
    return {"img":img_base64}


if __name__=="__main__":
    app.run(debug=True)