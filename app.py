from flask import Flask, render_template, request
from model import classifiable 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
	if request.method == 'POST':
		statement = request.form.get('statement')
		predicted = classifiable(statement)
		return render_template('predict.html', predicted=predicted)
	return render_template('index.html')

if __name__ == '__main__':
	app()