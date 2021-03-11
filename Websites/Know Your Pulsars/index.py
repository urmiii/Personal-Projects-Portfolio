#to install spicepy in anaconda, try following in anaconda cmd:
#conda install -c conda-forge spiceypy
import spiceypy
import datetime

from flask import Flask, render_template, flash, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateTimeField, DateField, FloatField
from wtforms.validators import DataRequired


#loading kernels
spiceypy.furnsh('naif0012.tls')
spiceypy.furnsh('de432s.bsp')

app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'
###################### CLASS    ##########################


class SimpleForm(FlaskForm):
	dt = DateField('DatePicker', format='%Y-%m-%d')
	submit = SubmitField('Submit here')



####################  ROUTES  ##########################
@app.route('/', methods=['GET','POST'])
def index():
	form = SimpleForm()

	if form.validate_on_submit():
		#converted datetime to string and display
		convt = form.dt.data.strftime('%m-%d-%Y')
		#converting utc to et
		et = spiceypy.utc2et(convt)	
		return str(et) #prints et
	return render_template('basic.html', form=form)

@app.route('/thankyou')
def distance():
	EARTH_STATE_WRT_SUN, EARTH_SUN_LT = spiceypy.spkgeo(targ=399, \
                                                    et=et, \
                                                    ref='ECLIPJ2000', obs=10)
	return str(pos_vel)







if __name__ == '__main__':
	app.run(debug=True)