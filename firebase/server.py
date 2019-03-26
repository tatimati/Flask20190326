from flask import Flask, render_template, request

import firebase_admin

from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("#自分のプロジェクトの秘密鍵#")

firebase_admin.initialize_app(cred, {
    'databaseURL': '#自分のプrジェクトのデータベース#',
    'databaseAuthVariableOverride': {
        'uid': 'I-am-Admin-year' #security id
    }
})

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def data_get_index():
	
	webtitle = 'firebase App'
	error_message = []
	
	if request.method == 'POST':
		getname = request.form['name']
		getpoint = request.form['point']
		
	
		
		#例外処理
		if getname == "":
			error_message.append("名前が入力されていません")
		
		if getpoint == "":
			error_message.append("点数が入力されていません")
		else:	
			try:
				int(getpoint)
			except ValueError:
				error_message.append("点数には整数を入力してください")
		
		if not error_message:
		
			subject_ref = db.reference('/subjects/').child(getname)
			subject_ref.update({
				'name' : getname,
				'point' : getpoint
				})
	
	
	
	subject_ref = db.reference('/subjects/')
	
	subject_data =  subject_ref.get()
	
	return render_template('index.html', title=webtitle, subject_data = subject_data, error_message=error_message)
	


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
	#app.run(port=8080)

