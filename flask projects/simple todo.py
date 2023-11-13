from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder="templates")

# Some initial tasks
tasks = ["Task 1", "Task 2", "Task 3"]

@app.route('/')
def index():
    return render_template('index1.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form['new_task']
    tasks.append(new_task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
