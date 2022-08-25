from flask import Flask, request, render_template
import numpy as np
import conf


# Declare a Flask app
app = Flask(__name__)


@app.route('/decode_pdf', methods=['POST'])
def decode_pdf():
	data = request.get_json(force=True)
	pdf_data = data['data']
	return pdf_data


@app.route('/decode_numpy', methods=['POST'])
def decode_numpy():
	data = request.get_json(force=True)
	pdf_data = data['data']
	return pdf_data


# Running the app
if __name__ == '__main__':
	print(f"Starting server at {conf.predict_url_local}")
	app.run(
		port=conf.port,
		debug=True
		)
