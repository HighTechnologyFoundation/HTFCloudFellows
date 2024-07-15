from datetime import datetime

from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    return render_template('index.html', date_time=date_time)

@app.route('/GFS')
def GFS():
    return render_template('GFS.html')

@app.route('/FirstStreet', methods=['POST', 'GET'])
def FirstStreet():
    disasters = ['Fire', 'Flood', 'Heat', 'Wind']
    regions = ['United States', 'West Virginia']
    if request.method == 'POST':
        a = request.form.get('disaster')
    return render_template('FirstStreet.html', disasters = disasters, regions = regions)

@app.route('/FirstStreet/test') 
def test(): 
    if request.method == 'POST':
        a = request.form.get('disaster')
    return str(a)

@app.route('/FirstStreet/plots') 
def return_img(): 
    # python code
    return 'FirstStreet_Flood_US_Bar.png' 

@app.route('/GHCN')
def GHCN():
    return render_template('GHCN.html')

@app.route('/GHCN/plotly')
def GHCN_plotly():
    return render_template('GHCN_plotly.html')

@app.route('/NSRDB_PySAM')
def NSRDB_PySAM():
    return render_template('NSRDB_PySAM.html')

@app.route('/Sup3rCC')
def Sup3rCC():
    return render_template('Sup3rCC.html')

@app.route('/USGS_Earthquake')
def USGS_Earthquake():
    return render_template('USGS-Earthquake.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)