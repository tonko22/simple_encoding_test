from flask import Flask, request, render_template
import numpy as np

# Declare a Flask app
app = Flask(__name__)


@app.route('/decode_pdf', methods=['POST'])
def decode_pdf():
	data = request.get_json(force=True)
	pdf_data = data['data']
	return pdf_data


@app.route('/decode_numpy', methods=['POST'])
def decode_pdf():
	data = request.get_json(force=True)
	pdf_data = data['data']
	return pdf_data


# Running the app
if __name__ == '__main__':
	app.run(
		port=9001,
		debug=True
		)
