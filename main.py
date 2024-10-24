from flask import Flask, render_template, request, redirect, send_file
from scrap import *
from file import save_to_file

#Flask에선 templates이라는 폴더를 찾도록 정해져있음
#request는 브라우저가 웹사이트에 가서 콘텐츠를 요청하는 기능

app = Flask("JobScrapper") #initialize app

@app.route("/") #decorator (when user goes to "/" route, run right below)
def home():
    return render_template("home.html")

db = {}

@app.route("/search")
def hello(): 
    keyword = request.args.get("keyword")
    if keyword == None: 
        return redirect("/") #flask에 있는 모듈 redirect
    if keyword in db: 
        job_db = db[keyword]
    else: 
        job_db = scrap(keyword)
        db[keyword] = job_db
    return render_template("search.html", keyword=keyword, jobs=job_db)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword]) #csv파일을 저장
    return send_file(f"{keyword}jobs.csv", as_attachment=True) #as_attachment=True: 다운로드 실행

app.run("0.0.0.0", port=8080)

