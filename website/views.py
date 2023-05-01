from flask import Blueprint, render_template, request
from .model import Note, Comment
from flask_login import login_user, login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/notes', methods=['POST', 'GET'])
def notes():
    if request.method == 'POST':
        note = request.form.get("note")
        if (note is not None):
            if len(note) > 1:
                n = Note(text=note, user_id=current_user.id)
                db.session.add(n)
                db.session.commit()
                print("СОЗДАНА НОВАЯ ЗАПИСЬ")

        comment = request.form.get("comment")
        note_id = request.form.get("note_id")
        if (comment is not None):
            if len(comment) > 1:
                c = Comment(text=comment, user_id=current_user.id, note_id=note_id)
                db.session.add(c)
                db.session.commit()
                print("СОЗДАНА НОВАЯ ЗАПИСЬ")



    notes = db.session.query(Note).order_by(Note.id.desc()).limit(10)
    comments = db.session.query(Comment).order_by(Comment.id.desc()).limit(10)
 
    return render_template("notes.html", notes=notes, comments=comments, user=current_user)


@views.route('/private_notes', methods=['POST', 'GET'])
@login_required
def private_notes():
    if request.method == 'POST':
        note = request.form.get("note")
        if (note is not None):
            if len(note) > 1:
                n = Note(text=note, user_id=current_user.id)
                db.session.add(n)
                db.session.commit()
                print("СОЗДАНА НОВАЯ ЗАПИСЬ")

        comment = request.form.get("comment")
        note_id = request.form.get("note_id")
        if (comment is not None):
            if len(comment) > 1:
                c = Comment(text=comment, user_id=current_user.id, note_id=note_id)
                db.session.add(c)
                db.session.commit()
                print("СОЗДАНА НОВАЯ ЗАПИСЬ")

    notes = db.session.query(Note).order_by(Note.id.desc()).limit(10)
    comments = db.session.query(Comment).order_by(Comment.id.desc()).limit(10)
 
    return render_template("private_notes.html", notes=notes, comments=comments, user=current_user)