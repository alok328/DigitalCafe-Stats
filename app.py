from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import numpy as np
import json
import data

app = Flask(__name__)

@app.route('/getStudentsMealWise', methods=['GET'])
def getStudentsMealWise():
    dataStatObj = data.Data()
    dataStatObj.makeData()
    response = None
    with open('mealWiseData.json', 'r') as fp:
        response = json.load(fp)
    if(response == None):
        return '<h2>Data file not found</h2>', 404    
    return jsonify(response)
    
@app.route('/getStudentsDayWise', methods=['GET'])
def getStudentsDayWise():  
    dataStatObj = data.Data()
    dataStatObj.dayWise()  
    response = None
    with open('dayWiseData.json', 'r') as fp:
        response = json.load(fp)
    if(response == None):
        return '<h2>Data file not found</h2>', 404    
    return jsonify(response) 

if __name__ == '__main__':
    app.run()