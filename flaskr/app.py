from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    return render_template('index.html', date_time=date_time)

@app.route('/GFS')
def GFS():
    return render_template('GFS.html')

@app.route('/FirstStreet')
def FirstStreet():
    return render_template('FirstStreet.html')

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