from flask import Flask, render_template, request
import serial
import time
import re
import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Pressure():

	webtitle = 'Pressure App'

	#現在時刻を取得
	now_time = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')

	# Arduinoがあるかどうかのチェック
	try:
		con = serial.Serial('/dev/ttyACM0', 9600) #9600の数字はArduino側のボーレートと同じ値です。
	except serial.serialutil.SerialException:
		emessage = "error!"
		return render_template('index.html', title=webtitle,  now_time=now_time, emessage=emessage)

	time.sleep(2)
	dummy=con.readline()     #最初に型番号が出力されるため、読み捨てる



	con.write(b'g') 	#Arduino側に命令を送っている。
	byte_data = con.readline()     #Arduinoが出力した文字列を一行取得
	print(byte_data) #デバッグ用

	#送られてくる順番は気圧、温度

	#正規表現で数字と小数点だけを抽出  数字と小数点以外の文字でデータが区切られる。

	pattern=r'([0-9]+\.?[0-9]*)'

	try:
		string_data = byte_data.decode('utf-8')
	except  UnicodeDecodeError:
		string_data = []
	#データがリストに格納される。
	data_list = re.findall(pattern, string_data)

	try :
		#リストからデータを取り出す
		#Arduino側から送られてくるデータの数によってここが変わるので注意!!!!!!!!!!!!
		pressure_data = data_list[0]
		temp_data = data_list[1]
	except IndexError:
		pressure_data = "None"
		temp_data = "None"



	return render_template('index.html', title=webtitle, pressure_data=pressure_data, temp_data=temp_data, now_time=now_time)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
