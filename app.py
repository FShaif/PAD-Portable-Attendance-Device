from flask import Flask, render_template
from postdata import posts
import pymysql.cursors
import os
from dotenv import load_dotenv

# Load environment variables from passwords.env file
load_dotenv('passwords.env')

# Retrieve environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')
m_password = os.getenv('M_PASSWORD')

# Create a MySQL connection
connection = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_password,
                             database=db_name,
                             port=int(db_port))  # Ensure port is cast to int

try:
    with connection.cursor() as cursor:
        # Test the connection
        cursor.execute('SELECT 1')
        print('Connected to the database')
except Exception as e:
    print('Error connecting to the database:', e)
    exit(1)  # Terminate the application

app = Flask(__name__)

# Page Routes
@app.route("/")
def homePagex():
   return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')

        
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/course")
def course():
    return render_template('course.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')
@app.route("/FAQ")
def FAQ():
    return render_template('FAQ.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404



    
#to get favicon working on layout instead of html page
import os
from flask import send_from_directory
from json import dumps

@app.route("/favicon.ico") 
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')




# Setting up Flask-Mail
from flask_mail import Mail, Message
from flask import request

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'ubttester1@gmail.com'
app.config['MAIL_PASSWORD'] = m_password

mail = Mail(app)

@app.route('/send_email', methods=['post'])
def send_reset_email(user_email):

   msg = Message('email title',
                 sender = 'noreply@demo.com',
                 recipients = [user_email] )

   msg.body = f'''
   	Hello { user_email }
   '''
   mail.send(msg)

#Implementing flask to the second form of the contact us page
@app.route('/contact_us', methods=['POST'])
def contact_us():
    name = request.form['Contact-Name']
    email = request.form['Contact-Email']
    message = request.form['Contact-Message']

    # Send email using Flask-Mail
    msg = Message('Contact Us Form Submission',
                  sender='noreply@demo.com',
                  recipients=['ubttester1@gmail.com'])
    msg.body = f'''
        Name: {name}
        Email: {email}
        Message: {message}
    '''
    mail.send(msg)

    # Return a success message to the user
    return 'Thank you for your message!'\
        '<a href="/contact"> Click here to submit another message.'\
        '</a> <br> Or click <a href="/index">Home</a> to return to the main page'

    # Define a route to retrieve and display the table data
@app.route('/AUTHENTICATION')
def AUTHENTICATION():
    # Specify your table name
    tableName = 'AUTHENTICATION'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500

@app.route('/COURSES')
def COURSES():
    # Specify your table name
    tableName = 'COURSES'  # Replace with the actual table name
    # Define the SQL query
    query = f'SELECT * FROM {tableName}'

    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
    
@app.route('/COURSES/SA0359')
def COURSESSA0359():
    # Specify your table name
    tableName = 'COURSES'  # Replace with the actual table name
    # Define the SQL query
    query = f"SELECT * FROM {tableName} WHERE Instructor_ID = 'SA0359' "

    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
@app.route('/COURSES/PB0086')
def COURSESPB0086():
    # Specify your table name
    tableName = 'COURSES'  # Replace with the actual table name


    # Define the SQL query
    query = f"SELECT * FROM {tableName} WHERE Instructor_ID = 'PB0086' "


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
@app.route('/USERS')
def USERS():
    # Specify your table name
    tableName = 'USERS'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500


    
@app.route('/ATTENDANCE')
def ATTENDANCE():
    # Specify your table name
    tableName = 'ATTENDANCE'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
    
@app.route('/SOFTWARE_MAINTENANCE_AND_EVOLUTION_1_02')
def SOFTWARE_MAINTENANCE_AND_EVOLUTION_1_02():
    # Specify your table name
    tableName = 'SOFTWARE_MAINTENANCE_AND_EVOLUTION_1_02'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
    
@app.route('/SOFTWARE_MAINTENANCE_AND_EVOLUTION_2_02')
def SOFTWARE_MAINTENANCE_AND_EVOLUTION_2_02():
    # Specify your table name
    tableName = 'SOFTWARE_MAINTENANCE_AND_EVOLUTION_2_02'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
    
@app.route('/INTERNET_APPLICATION_1_01')
def INTERNET_APPLICATION_1_01():
    # Specify your table name
    tableName = 'INTERNET_APPLICATION_1_01'  # Replace with the actual table name


    # Define the SQL query
    query = f'SELECT * FROM {tableName}'


    try:
        with connection.cursor() as cursor:
            # Execute the SQL query
            cursor.execute(query)
            # Get column names
            column_names = [desc[0] for desc in cursor.description]
            # Fetch all rows
            rows = cursor.fetchall()
            # Convert row data to dictionary
            results = [dict(zip(column_names, row)) for row in rows]
            # Render the table with the data
            return render_template('tables.html', data=results)
    except Exception as e:
        print('Error retrieving table data:', str(e))
        return 'Error retrieving table data', 500
#debug tool
if __name__ == '__main__':
	app.run( debug=True )

