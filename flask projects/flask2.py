# combining  html to the flask

from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def welcome():
    return render_template('index.html')

if __name__=="__main__":

    app.run(debug=True)