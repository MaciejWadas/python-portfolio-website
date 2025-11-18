from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditorField,CKEditor
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, mapped_column
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_PATH = os.getenv("DB_PATH")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)

Bootstrap5(app)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Project(db.Model):
    __tablename__ = 'projects'
    id = mapped_column(db.Integer, primary_key=True)
    title = mapped_column(db.String,unique=True)
    description = mapped_column(db.String)
    short_description = mapped_column(db.String)
    img_link = mapped_column(db.String)
    github_link = mapped_column(db.String)

with app.app_context():
    db.create_all()

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    short_description = StringField('Subtitle', validators=[DataRequired()])
    img_link = StringField('Image Link', validators=[DataRequired(), URL()])
    github_link = StringField('GitHub Link', validators=[DataRequired(), URL()])
    description = CKEditorField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    projects = db.session.execute(db.select(Project)).scalars().all()
    print(projects)
    return render_template("portfolio.html",projects=projects)

@app.route('/about')
def about_me():
    return render_template("about_me.html")

@app.route('/add-project', methods=['GET', 'POST'])
def add_project():
    project_form = ProjectForm()
    if request.method == 'POST':
        try:
            if project_form.validate_on_submit():
                title = project_form.title.data
                description = project_form.description.data
                short_description = project_form.short_description.data
                img_link = project_form.img_link.data
                github_link = project_form.github_link.data
                project = Project()
                project.title = title
                project.short_description = short_description
                project.description = description
                project.img_link = img_link
                project.github_link = github_link

                with app.app_context():
                    db.session.add(project)
                    db.session.commit()
                return redirect(url_for('portfolio'))
        except IntegrityError:
            flash("The name of a post must be unique!", "error")
    return render_template("add_project.html",form=project_form)

@app.route("/project/<int:id>")
def show_project(id):
    project = Project.query.get_or_404(id)
    return render_template("project.html", project=project)

if __name__ == "__main__":
    app.run(debug=True, port=5001)