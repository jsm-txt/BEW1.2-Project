from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_user, logout_user, login_required, current_user

from pet_app.models import User, Pet, Image
from pet_app.forms import SignUpForm, LoginForm, NewPetForm, ImagesForm



# Import app and db from events_app package so that we can run app
from pet_app import app, db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
main = Blueprint("main", __name__)


##########################################
#           Routes                       #
##########################################
# def create_pet():
#     new_pet = Pet(name='Polo', id=1)
#     db.session.add(new_pet)
#     db.session.commit()
# create_pet()

@main.route('/')
def homepage():
    
    all_pets = Pet.query.all()
    print(all_pets)
    
    return render_template('home.html', all_pets=all_pets )












# routes.py

auth = Blueprint("auth", __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    print('in signup')
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Account Created.')
        print('created')
        return redirect(url_for('auth.login'))
    print(form.errors)
    return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('main.homepage'))
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))