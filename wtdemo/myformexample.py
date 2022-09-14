from flask import Flask,render_template
from myformclass import NameForm
from werkzeug.utils import secure_filename


app=Flask(__name__)

#including a secret key to prevent CSRF attacks in the app.config dictionary
app.config['SECRET_KEY'] = 'secret string'

@app.route('/enquiry',methods = ['GET','POST'])
def enquiry():
    #create an instance of NameForm class from myformclass.py
    form = NameForm()
    name = None
    #checking if all the validators were passed and the form was submitted
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        filename = secure_filename(form.filename.data.filename)
        form.filename.data.save('uploads/'+filename)
    return render_template('enquiry.html', form=form, name=name)

if __name__ == '__main__':
    app.run(debug=True)