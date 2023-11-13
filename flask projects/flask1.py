from flask import Flask
app=Flask(__name__)
@app.route('/')

def welcome_page():
    return "welcome "
if __name__=='__main__':
    app.run(debug=True)

