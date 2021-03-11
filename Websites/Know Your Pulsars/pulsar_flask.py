from flask import Flask, render_template, request
from astropy.io import fits
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os
import glob
from flask import flash
import uuid
import numpy as np
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

		#for filename in glob.glob(os.path.join(folder_path, '*.fits')):
		#with open(filename, 'r') as f:
		#flash (filename)
import os
@app.route('/')
def home():
	folder_path = 'uploads/'
	for filename in glob.glob(os.path.join(folder_path, '*.fits')):
		#with open(filename, 'r') as f:
		#flash (filename)
		hdu = fits.open(filename)[0]
		plt.figure(figsize=(6,6))
		plt.imshow(hdu.data, origin='lower')



		filename_new = str(uuid.uuid4())

		save_path =  "display/"  + filename_new + ".png"
		plt.savefig(save_path)


	return render_template('upload.html')



if __name__ == '__main__':
   app.run(debug = True)