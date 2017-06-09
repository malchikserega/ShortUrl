from ShortUrl import app
from flask import render_template
from flask import request
from flask import redirect
from scripts.shortenerutils import getshorturl
from urllib.parse import urlparse
from db_functions import *
import config


@app.route('/', methods=['GET', 'POST'])
def shortener():
    return render_template('base.html')


@app.route('/shturl', methods=['POST'])
def shturl():
    url = request.form['url']
    if url != '':
        short_url = getshorturl(url=url)
        add_url(origin_url=url, shurl=short_url)
        return short_url
    else:
        return False


@app.route('/<short_url>')
def redirect_url(short_url):
    url = config.HOST
    try:
        url = get_url(shurl=short_url)
        if url is not False:
            url_parts = urlparse(url=url)
            if url_parts.scheme == 'http' or url_parts.scheme == 'https':
                return redirect(url, code=302)
            else:
                return redirect('http://' + url, code=302)
    except Exception as e:
        print(e)
    return redirect(url, code=302)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
