# Portfolio
# got html template from: http://www.mashup-template.com/templates.html

# in order to clone your git portfolio to your device, install git, add it to environmental variables
# go to your website directory and use command: git clone (copied link from your repo on github
# https://github.com/bahaa-abouzahr/portfolio.git

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')  # home route /
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')  # so you can input page name
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # opening database in mode append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'Email: {email}\nSubject: {subject}\nMessage: {message}\n\n')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:  # opening database in mode append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

# go to web server folder using cmd, and type: flask --app Web_Server.py --debug run
# debug mode can give errors, and also live update! just save file and refresh
# without it, you need to re-run server command again and again
