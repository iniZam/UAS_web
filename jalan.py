from flask import Flask,render_template # remder tempalte itu berguna untuk memanggil halaman html yang berada di dalam folder templates

app = Flask(__name__)

data_orang = [ #ini adalah sebuah data bertipe dictonary
	{'nama': 'Bambang ',
	'gender': 'batang',
	'spesies':'manusia (mungkin)'}
	,
	{'nama': 'Otong ',
	'gender': 'batang',
	'spesies':'manusia (yang pasti bukan binatang)'}	
	]

@app.route("/")# yang di dalam ini adalah parameter dan tanda (/) adalah parameter default. maksudnya saat servernya dijalankan maka yang ini akan langsung dijalankan 
def rumah ():
	return render_template("anjay.html")#ini adalah cara untuk memanggil file htmlnya 

@app.route('/login') # jika setelah dijalankan terus di linknya ditambahkan sesuai parameternya maka halaman yang terbuka akan sesuai dengan yang ada di defnya 
def login():
	return render_template("latihanlogin.html")

@app.route("/data")
def data():
	return render_template("data_orang.html",anjay=data_orang) #variabel anjay  yang pertama itu namanya bebas yang penting variabel yang keduanya(data_orang) sudah ada di atas. dan ini berguna agar data/variabelnya bisa kepanggil di file html 

@app.route('/memo')
def memo():
	return render_template ("tentang.html")

@app.route('/artikel') 
def artikel():
	return render_template("data_orang.html")

@app.route('/artikel/<info>') # ini akan mengambil parameter tambahan yang diletakan di url(link). cara pakainya itu tinggal tulis nama parameternya setelah artikel (artikel/"parameternya") di link. dan yang ada di dalam kurung juga adalah rumusnya 
def artikel_info(info): # yang di dalam kurung adalah parameter tambahan jadi dia apapun yang ditulis di link akan menjadi nilai dari info
	return "halaman artikel "+info #info ini dipanggil sesuai dengan apa yang tertulis di link (anggap saja variabel bebas)


if __name__=="__main__":
	app.run(debug=True)