# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def jsonified():
    return "Precipitation!"


@app.route("/api/v1.0/stations")
def jsonified():
    return "Stations!"


@app.route("/api/v1.0/tobs")
def normal():
    return "Tobs!"


if __name__ == '__main__':
    app.run(debug=True)
