from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def post_test():
	webtitle = 'POST Test'
	if request.method == 'POST':
		getnum = request.form['num']

		# 入力されたデータが整数かどうか判別
		try :
			getnum = int(getnum) #change string into int
		except ValueError as e:
			message = 'error!!!!!! Please enter an integer!!!!!!'
			return render_template('index.html',title = webtitle, message = message)

		# 偶数奇数判定
		if getnum % 2 == 0:
			result = 'even'
		elif getnum %2 == 1:
			result = 'odd'
		else :
			result = 'error'
			
		return render_template('index.html',title = webtitle,num = getnum, result = result)
	
	else:
		return render_template('index.html',title = webtitle)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
