from flask import Flask, render_template, request

import numpy as np

app = Flask(__name__)

result = ['★★', '★★★', '★★★★']
probability=['0.9','0.07','0.03']

#ガチャのデータを扱うクラス
class  Gatya_data(object):
	
	def __init__ (self):
		self._spent_money = 0
		self._Count_Double_Rare = 0 # ★★
		self._Count_Triple_Rare = 0 # ★★★
		self._Count_Quadruple_Rare = 0 # ★★★★
	
	#@spent_money.getter
	@property
	def spent_money(self):
		return self._spent_money
	
	@spent_money.setter
	def spent_money(self, set_value):
		self._spent_money = set_value
	
	@property
	def Count_Double_Rare(self):
		return self._Count_Double_Rare

	@Count_Double_Rare.setter
	def Count_Double_Rare(self, set_value):
		self._Count_Double_Rare = set_value
		
	@property
	def Count_Triple_Rare(self):
		return self._Count_Triple_Rare
	
	@Count_Triple_Rare.setter
	def Count_Triple_Rare(self, set_value):
		self._Count_Triple_Rare = set_value

	@property
	def Count_Quadruple_Rare(self):
		return self._Count_Quadruple_Rare
	
	@Count_Quadruple_Rare.setter
	def Count_Quadruple_Rare(self, set_value):
		self._Count_Quadruple_Rare = set_value
		
	def gatya_result_add(self, result):
		if result == '★★':
			self.Count_Double_Rare = self.Count_Double_Rare + 1
			
		elif result == '★★★':
			self.Count_Triple_Rare = self.Count_Triple_Rare + 1
			
		elif result == '★★★★':
			self.Count_Quadruple_Rare = self.Count_Quadruple_Rare + 1

	
#return gatya result
def  lottery():
	return np.random.choice(result, p=probability)
	
#ガチャ抽選機能
def gatya_function(gatya_items, gatya_data):
	result_item = lottery()
	gatya_data.gatya_result_add(result_item)
	gatya_items.append(result_item)
	
#インスタンス化
gatya_data = Gatya_data ()

@app.route('/',methods=['GET','POST'])
def gatya_index():
	
	webtitle = 'Gatya'
	gatya_items = []	
	
	if request.method == 'POST':
		
		
		#postの中にonceがあったら真
		if "once" in request.form:
			gatya_function(gatya_items, gatya_data)
			
		elif "ten" in request.form:
			for i in range(10):
				gatya_function(gatya_items, gatya_data)
		
		elif "reset":
			 gatya_data.Count_Double_Rare = 0
			 gatya_data.Count_Triple_Rare = 0
			 gatya_data.Count_Quadruple_Rare = 0	
				
	return render_template('index.html', title=webtitle, gatya_data = gatya_data, gatya_items=gatya_items)
		

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)


