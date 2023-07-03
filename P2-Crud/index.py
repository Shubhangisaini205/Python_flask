from flask import Flask, render_template, request, redirect

app = Flask(__name__)
entries = {}  # Python dictionary to store the data


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        entries[key] = value
        print(entries,'create')
        return redirect('/read')
    return render_template('create.html')


@app.route('/read')
def read():
    print(entries,'read')
    return render_template('read.html', entries=entries)


@app.route('/update', methods=['GET', 'POST'])
def update():
    key=request.args.get('key')
    if request.method == 'POST':
        value = request.form.get('value')
        key = request.form.get('key')
        entries[key] = value
        print
        (key,value,'update')
        return redirect('/read')

    return render_template('update.html', key=key, value=entries[key])


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in entries:
            del entries[key]
        return redirect('/read')
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
