import os
from flask import Flask, request, jsonify, send_from_directory
from json import dumps, loads
import pandas as pd
import urllib.request, json 
from io import StringIO

app = Flask(__name__, static_folder=".", template_folder=".")

url_ywc = "https://ywc15.ywc.in.th/api/interview"

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response

@app.route("/")
def home():
    return send_from_directory("./web-content/", "index.html")

@app.route("/css/bootstrap.css")
def home1():
    return send_from_directory("./web-content/", "css/bootstrap.css")

@app.route("/js/jquery-1.7.1.min.js")
def hom1():
    return send_from_directory("./web-content/", "js/jquery-1.7.1.min.js")

@app.route("/js/d3.v3.min.js")
def hon1():
    return send_from_directory("./web-content/", "js/d3.v3.min.js")

@app.route("/css/thin-admin.css")
def home2():
    return send_from_directory("./web-content/", "css/thin-admin.css")

@app.route("/css/font-awesome.css")
def home3():
    return send_from_directory("./web-content/", "css/font-awesome.css")

@app.route("/style/style.css")
def home4():
    return send_from_directory("./web-content/", "style/style.css")

@app.route("/images/a.jpg")
def home44():
    return send_from_directory("./web-content/", "images/a.jpg")

@app.route("/images/logo.png")
def home445():
    return send_from_directory("./web-content/", "images/logo.png")

@app.route("/images/programming.png")
def programming():
    return send_from_directory("./web-content/", "images/programming.png")

@app.route("/images/marketing.png")
def marketing():
    return send_from_directory("./web-content/", "images/marketing.png")

@app.route("/images/content.png")
def content():
    return send_from_directory("./web-content/", "images/content.png")

@app.route("/images/design.png")
def design():
    return send_from_directory("./web-content/", "images/design.png")

@app.route("/style/dashboard.css")
def home5():
    return send_from_directory("./web-content/", "style/dashboard.css")

# @app.route("/d3csv")
# def home65():
#     return send_from_directory("./web-content/", "js/d3csv.js")

@app.route("/assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css")
def home6():
    return send_from_directory("./web-content/", "assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css")

# @app.route("/data/interview")
# def interview():
#     return send_from_directory("./web-content/", "data/interview")

@app.route("/query/<string:id>")
def query(id):
    # url_ywc = "https://ywc15.ywc.in.th/api/interview"
    with urllib.request.urlopen(url_ywc) as url:
        data = json.loads(url.read().decode())
        stra = "interviewRef,firstName,lastName\n"
        # str = ""
        for d in data:
            if(d['major']==id):
                stra = stra +d['interviewRef']+","+d['firstName']+","+d['lastName']+"\n"
        TESTDATA = StringIO(stra)
        df = pd.read_csv(TESTDATA)
        df = df.sort_values(by=['interviewRef'], ascending=[True])
        df['interviewTime'] = 'ช่วงบ่าย'
        if id=='programming':
            df.loc[df.interviewRef.str[2:].astype(int)<=23, 'interviewTime'] = 'ช่วงเช้า'
        if id=='marketing':
            df.loc[df.interviewRef.str[2:].astype(int)<=18, 'interviewTime'] = 'ช่วงเช้า'
        if id=='design':
            df.loc[df.interviewRef.str[2:].astype(int)<=20, 'interviewTime'] = 'ช่วงเช้า'
        if id=='content':
            df.loc[df.interviewRef.str[2:].astype(int)<=25, 'interviewTime'] = 'ช่วงเช้า'
        print(df.interviewTime)
        s = df.to_csv(index=False,header=None)
        return s
    
@app.route("/images/dek-d")
def s1():
    return send_from_directory("./web-content/", "images/dek-d.png")

@app.route("/images/lnw")
def s2():
    return send_from_directory("./web-content/", "images/lnw.png")

@app.route("/images/mango-zero")
def s3():
    return send_from_directory("./web-content/", "images/mango-zero.png")

@app.route("/images/p_t")
def s4():
    return send_from_directory("./web-content/", "images/p_t.png")

@app.route("/images/pantip")
def s5():
    return send_from_directory("./web-content/", "images/pantip.png")

@app.route("/images/s_cpall")
def s6():
    return send_from_directory("./web-content/", "images/s_cpall.png")

@app.route("/images/s_pim")
def s7():
    return send_from_directory("./web-content/", "images/s_pim.png")

@app.route("/images/s_scb")
def s8():
    return send_from_directory("./web-content/", "images/s_scb.png")

@app.route("/images/s_twa")
def s9():
    return send_from_directory("./web-content/", "images/s_twa.png")

@app.route("/images/tencent")
def s10():
    return send_from_directory("./web-content/", "images/tencent.png")

@app.route("/images/wongnai")
def s11():
    return send_from_directory("./web-content/", "images/wongnai.png")

@app.route("/images/fb")
def fb():
    return send_from_directory("./web-content/", "images/fb.png")

@app.route("/images/tw")
def tw():
    return send_from_directory("./web-content/", "images/tw.png")

@app.route("/images/ig")
def ig():
    return send_from_directory("./web-content/", "images/ig.png")

@app.route("/images/yt")
def yt():
    return send_from_directory("./web-content/", "images/yt.png")

@app.route("/images/bank")
def bank():
    return send_from_directory("./web-content/", "images/guru/bank-design.jpg")

@app.route("/images/boy")
def boy():
    return send_from_directory("./web-content/", "images/guru/boy-content.jpg")

@app.route("/images/bung")
def bung():
    return send_from_directory("./web-content/", "images/guru/bung-programming.jpg")

@app.route("/images/earth")
def earth():
    return send_from_directory("./web-content/", "images/guru/earth-design.jpg")

@app.route("/images/go")
def go():
    return send_from_directory("./web-content/", "images/guru/go-content.jpg")

@app.route("/images/hunt")
def hunt():
    return send_from_directory("./web-content/", "images/guru/hunt-programming.jpg")

@app.route("/images/j")
def j():
    return send_from_directory("./web-content/", "images/guru/j-marketing.jpg")

@app.route("/images/jib")
def jib():
    return send_from_directory("./web-content/", "images/guru/jib-marketing.jpg")

@app.route("/images/m")
def m():
    return send_from_directory("./web-content/", "images/guru/m-content.jpg")

@app.route("/images/men")
def men():
    return send_from_directory("./web-content/", "images/guru/men-design.jpg")

@app.route("/images/neung")
def neung():
    return send_from_directory("./web-content/", "images/guru/neung-design.jpg")

@app.route("/images/ong")
def ong():
    return send_from_directory("./web-content/", "images/guru/ong-marketing.jpg")

@app.route("/images/panj")
def panj():
    return send_from_directory("./web-content/", "images/guru/panj-programming.jpg")

@app.route("/images/pom")
def pom():
    return send_from_directory("./web-content/", "images/guru/pom-marketing.jpg")

@app.route("/images/pond")
def pond():
    return send_from_directory("./web-content/", "images/guru/pond-design.jpg")

@app.route("/images/pong")
def pong():
    return send_from_directory("./web-content/", "images/guru/pong-content.jpg")

@app.route("/images/thang")
def thang():
    return send_from_directory("./web-content/", "images/guru/thang-programming.jpg")

@app.route("/images/wan")
def wan():
    return send_from_directory("./web-content/", "images/guru/wan-marketing.jpg")





if __name__ == "__main__":
	app.run()

