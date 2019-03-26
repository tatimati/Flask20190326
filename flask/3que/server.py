from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/') #POSTリクエストができるように変更する#
def post_test():
	
	webtitle = 'POST App'

	if #requestがPOSTだったら#:
		send_data = #ここにPOSTされたデータを受け取れるようにする。 データの名前はsend_data#
		return render_template('index.html', title=webtitle, send_data = send_data)

	
	return render_template('index.html', title=webtitle)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)

