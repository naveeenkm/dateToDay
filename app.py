from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route and its corresponding function
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/datepicker',methods=['GET', 'POST'])
def datepicker():
    day_of_week = ""
    if request.method == 'POST':
        year = request.form.get('year')
        month = request.form.get('month')
        day = request.form.get('day')
        date = f"{day}-{month}-{year}"
        day_of_week = predictDay(date)
        return render_template('datepicker.html', day_of_week=day_of_week,selected_date=date)
    return render_template('datepicker.html')
# Run the Flask app



def oddDays(year):
    odd = 0
    if int(year[:2]) % 4 == 1:
        odd += 5
    elif int(year[:2]) % 4 == 2:
        odd += 3
    elif int(year[:2]) % 4 == 3:
        odd += 1
    odd += int(year[2:])
    odd += int(int(year[2:]) / 4)
    return odd

def leapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False

def predictDay(date):
    date = date.split("-")
    month = {'01': 6, '02': 2, '03': 2, '04': 5, '05': 0, '06': 3, '07': 5, '08': 1, '09': 4, '10': 6, '11': 2, '12': 4}
    days = {'0': "Sunday", '1': "Monday", '2': "Tuesday", '3': "Wednesday", '4': "Thursday", '5': "Friday", '6': "Saturday"}
    odddays = int(date[0])
    odddays += month[date[1]]
    yearodddays = oddDays(str(date[2]))
    odddays += yearodddays
    if leapyear(int(date[2])) and (date[1] == '01' or date[1] == '02'):
        odddays -= 1
    odddays = odddays % 7
    return days[str(odddays)]



