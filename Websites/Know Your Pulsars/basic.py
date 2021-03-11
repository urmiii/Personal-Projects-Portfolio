from flask import Flask, render_template, session, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,  DateTimeField, DateField, FloatField, validators
from wtforms.validators import DataRequired
import spiceypy
import datetime
import math



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

####################ORBITAL SPEED AND DISTANCE####################################


#loading kernels
spiceypy.furnsh('naif0012.tls')
spiceypy.furnsh('de432s.bsp')

# Model
class Info(FlaskForm):
	dt = DateField('DatePicker',format='%Y-%m-%d')
	submit = SubmitField('Submit')

#Route
@app.route('/',methods=['GET','POST'])
def index():
	form = Info()

	if request.method == 'POST' and form.validate():

		#converted datetime to string and display
		convt = form.dt.data.strftime('%m-%d-%Y')
		#converting utc to et
		et = spiceypy.utc2et(convt)	
	
		EARTH_STATE_WRT_SUN, EARTH_SUN_LT = spiceypy.spkgeo(targ=399, \
                                                    et=et, \
                                                    ref='ECLIPJ2000', obs=10)

		#distance in km
		earth_sun_km = math.sqrt(EARTH_STATE_WRT_SUN[0]**2.0 \
                             + EARTH_STATE_WRT_SUN[1]**2.0 \
                             + EARTH_STATE_WRT_SUN[2]**2.0)

		#distance in au
		EARTH_SUN_DISTANCE_AU = spiceypy.convrt(earth_sun_km, 'km', 'AU')

		#oribtal speed
		EARTH_ORB_SPEED_WRT_SUN = math.sqrt(EARTH_STATE_WRT_SUN[3]**2.0 \
                                  + EARTH_STATE_WRT_SUN[4]**2.0 \
                                  + EARTH_STATE_WRT_SUN[5]**2.0)


		return render_template('output.html',form=form, et=et, convt=convt, EARTH_SUN_DISTANCE_AU=EARTH_SUN_DISTANCE_AU, EARTH_ORB_SPEED_WRT_SUN=EARTH_ORB_SPEED_WRT_SUN
				)

	return render_template('output.html',form=form)


####################PULSAR DETECTION####################################



#1. MULTIPLE FILE UPLOAD-START
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename



app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads does not exist
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['fits', 'png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('output.html')


@app.route('/uploader', methods=['POST'])
def upload_file():

	if request.method == 'POST':

		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')

		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#flash('File(s) successfully uploaded')



		return redirect('/Stacking')

#1. MULTIPLE FILE UPLOAD-END
#2. Converting FITS into Images and Stacking it via median and getting the output in png format -START

import glob
import uuid
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
##Saving the Stacked Image into the static/images folder
@app.route('/Stacking')
def home():
	folder_path = 'uploads/'
	image_concat = [fits.getdata(filename) for filename in glob.glob(os.path.join(folder_path, '*.fits'))]
	
	a = np.median(image_concat, axis = 0)
	plt.figure(figsize=(6,6))
	plt.imshow(a)

	filename_new = str(uuid.uuid4())
	save_path =  "static/images/"  + filename_new + ".png"
	plt.savefig(save_path)

	return redirect('/displayFile')

##Getting the path of the image
@app.route('/displayFile')
def displayFile():
	path_folder = 'static/images/'
	for file in glob.glob(os.path.join(path_folder,'*.png')):
		with open(file, 'r') as f:
			name = file
			#flash(name)

			head, tail = os.path.split(name)
			#flash(tail)


	return render_template('displayfile.html', user_image = tail)

#2. Converting FITS into Images and Stacking it via median and getting the output in png format -END


		
if __name__ == '__main__':
 	app.run(debug=True)










