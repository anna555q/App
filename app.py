from flask import Flask, render_template


app =  Flask(__name__)

users= {'RED':'0','BLUE':'1','BLACK':'2'}

def index():
    return render_template('index.html', title='Welcome', members=users)

@app.route("/")
def index():
    return render_template ('index.html', members=users)

if __name__ == '__main__':
    app.run(debug=True)

