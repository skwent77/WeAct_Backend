from flask import Blueprint,render_template
from flask import request
classes=Blueprint('classes',__name__,template_folder='templates/classes')

@classes.route('/class/list')
def getClassesList():
    return render_template('post.html')

@classes.route('/classes',methods=['POST'])
def postClasses():
    value=request.form['classesPost']
    return value
def deleteClasses():




