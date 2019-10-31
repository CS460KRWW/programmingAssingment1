#where files are loaded and components loaded
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
#import pages


app = Flask(__name__)

app.config['SECRET_KEY'] = '7429e37abbb9530cce0310c81e672614'
#relative path to current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'

#css static styling
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = 'static'

#database instance
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect = True)

business = Base.classes.Business 


#no circular imports
from codebase import routes