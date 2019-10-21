#where files are loaded and components loaded
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import pages


app = Flask(__name__)


#relative path to current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'

#css static styling
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = 'static'

#database instance
db = SQLAlchemy(app)

#no circular imports
from codebase import routes