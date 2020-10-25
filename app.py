from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    city_name = request.args.get('city')
    if not city_name:
        return render_template('index.jn')
    rep=requests.post('https://data.gov.il/api/3/action/datastore_search',json = {'filters': {'City':city_name},'limit':'99999', 'resource_id': '1c5bc716-8210-4ec7-85be-92e6271955c2','include_total':'true','fields':'Bank_Code,Bank_Name,Branch_Address,Branch_Code,City,Telephone,X_Coordinate,Y_Coordinate'})
    data = rep.json()['result']
    return  render_template('index.jn' ,result=True, bank_data=data)