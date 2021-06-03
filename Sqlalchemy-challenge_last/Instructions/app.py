import numpy as np
import sqlalchemy
import datetime as dt
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

##############################
# Database Setup
##############################
engine = create_engine('sqlite:///hawaii.sqlite')

##############################
#Reflect an existing database into a new model
##############################
Base = automap_base()

#Reflect the tables
Base.prepare(engine, reflect=True)

#Save refrence into tables
Measurement = Base.classes.measurement
Station = Base.classes.station
print(Base.classes.keys())
session = Session(engine)
app = Flask(__name__)
################################
# Creating a flask
################################
@app.route("/")
def welcome():
    """List all available API routes"""
    return (
        f"Available Routes:"
    )
    
#################################
#Converting the query results to a dictionary
#using date as key and prcp as value
#################################

@app.route("/api/v1.0/precipitation")
def precipitation():

    last_tweleve_months = dt.date(2017,8,23)- dt.timedelta(days=365)
    
    p_s_data= session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=last_tweleve_months).all()
    return jsonify(p_s_data) 

###################################
#Return the JSON representation of your dictionary.
###################################

@app.route("/api/v1.0/stations")
def stations():
    total_s= session.query(func.count(Station.station)).all()
    return jsonify (total_s)

###################################    
#Return a JSON list of temperature observation (TOBS)
#for the previous year
####################################

#@app.route("/api/v1.0/<start>")
#def startDate ():




if __name__== "__main__":
  app.run(debug=True) 

    

