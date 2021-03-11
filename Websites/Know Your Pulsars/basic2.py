from flask import Flask, render_template, session, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,  DateTimeField, DateField, FloatField, validators
from wtforms.validators import DataRequired
import spiceypy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#loading kernels
spiceypy.furnsh('naif0012.tls')
spiceypy.furnsh('de432s.bsp')

# Model
class Info(FlaskForm):
	submit = SubmitField('Submit')


#Route
@app.route('/',methods=['GET','POST'])
def index():
	form = Info()
	if request.method == 'POST' and form.validate():
		dt = DateField('DatePicker',format='&Y-%m-%d')
		convt = form.dt.data.strftime('%m-%d-%Y')

		return redirect(url_for('output'))


@app.route('/output')
def output():
	return render_template('output.html',form=form, convt=convt)

if __name__ == '__main__':
	app.run(debug=True)