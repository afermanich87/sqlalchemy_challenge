from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import numpy as np
import pandas as pd
import datetime as dt

app = Flask(__name__)

# establish connectioin to database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# specify routes
@app.route("/")
def home():
    return(
        f"welcome to climate analysis API"
        f"select from  the below routes"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/start/end"
          )



if __name__ == '__main__':
    app.run(debug=True)