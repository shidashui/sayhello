from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm


#界面视图
@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()#降序获取所有消息
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('您的消息已发布！')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)