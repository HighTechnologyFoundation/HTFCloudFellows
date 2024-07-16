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
    dis = request.form.get("disaster")
    reg = request.form.get("region")
    file = 'First-Street-Logo-Old.png'
    map_file = 'First-Street-Logo-Old.png'
    if dis == 'Fire' and reg == 'West Virginia':
        file = 'FirstStreet_Fire_WV_Bar.png'
        map_file = 'FirstStreet_Fire_WV_Map.png'
    if dis == 'Fire' and reg == 'United States':
        file = 'FirstStreet_Fire_US_Bar.png'
        map_file = 'FirstStreet_Fire_US_Map.png'
    if dis == 'Heat' and reg == 'West Virginia':
        file = 'FirstStreet_Heat_WV_Bar.png'
        map_file = 'FirstStreet_Heat_WV_Map.png'
    if dis == 'Heat' and reg == 'United States':
        file = 'FirstStreet_Heat_US_Bar.png'
        map_file = 'FirstStreet_Heat_US_Map.png'
    if dis == 'Flood' and reg == 'West Virginia':
        file = 'FirstStreet_Flood_WV_Bar.png'
        map_file = 'FirstStreet_Flood_WV_Map.png'
    if dis == 'Flood' and reg == 'United States':
        file = 'FirstStreet_Flood_US_Bar.png'
        map_file = 'FirstStreet_Flood_US_Map.png'
    if dis == 'Wind' and reg == 'West Virginia':
        file = 'FirstStreet_Wind_WV_Bar.png'
        map_file = 'FirstStreet_Wind_WV_Map.png'
    if dis == 'Wind' and reg == 'United States':
        file = 'FirstStreet_Wind_US_Bar.png'
        map_file = 'FirstStreet_Wind_US_Map.png'
    return render_template('FirstStreet.html', disasters = disasters, regions = regions, file = file, map_file = map_file)


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