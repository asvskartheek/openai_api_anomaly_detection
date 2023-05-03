import requests
import os
import sqlite3
from datetime import datetime, timedelta
from fbprophet import Prophet
import pandas as pd
import smtplib

api_key = os.environ.get('API_KEY')
headers = {
        'Authorization': f'Bearer {api_key}'
}

URL = "https://api.openai.com/v1/usage"

def make_api_call(date: str):
    """
    Makes an API call with a 'date' parameter and an Authorization header with a bearer token taken from an
    environment variable called 'API_KEY'.
    """
    # Get the API key from the environment variable
    date = datetime.now().strftime('%Y-%m-%d')
    params = {
        'date': date
    }
    response = requests.get(URL, headers=headers, params=params)
    n_requests = response.json()['data'][-1]['n_requests']
    
    return n_requests

def get_historical_data():
    """
    Makes 365 API calls with a 'date' parameter and an Authorization header with a bearer token
    taken from an environment variable called 'API_KEY'. Stores the data in a local SQLite database file.
    """
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data 
                      (date TEXT, n_requests INTEGER)''')

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    while start_date <= end_date:
        date = start_date.strftime('%Y-%m-%d')
        params = {
            'date': date
        }

        response = requests.get(URL, headers=headers, params=params)
        data_point = response.json()['data'][0]
        date = data_point['date']
        n_requests = data_point['n_requests']
        cursor.execute('INSERT INTO data VALUES (?, ?)', (date, n_requests))
        start_date += timedelta(days=1)

    # Commit the changes
    conn.commit()

    # Close the database connection
    conn.close()


def detect_anomaly(current_value):
    """
    Loads the timeseries data of the last 365 days from a local SQLite database file called 'data.db' and performs
    anomaly detection using the Prophet time series forecasting library. Returns True if the current value is an
    anomaly, and False otherwise.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')

    # Load the data into a pandas dataframe
    data = pd.read_sql_query('SELECT * FROM data', conn)

    # Prepare the data for Prophet
    data.columns = ['ds', 'y']
    data['ds'] = pd.to_datetime(data['ds'])

    # Fit the Prophet model to the data
    model = Prophet()
    model.fit(data)

    # Make a prediction for the current value
    future = pd.DataFrame({'ds': [pd.to_datetime('now')], 'y': [current_value]})
    forecast = model.predict(future)
    predicted_value = forecast['yhat'].values[0]

    # Determine if the current value is an anomaly
    max_value = data['y'].max()
    anomaly_threshold = max_value * 1.2  # Set the anomaly threshold to 20% above the maximum observed value
    is_anomaly = predicted_value > anomaly_threshold

    # Close the database connection
    conn.close()

    return is_anomaly

def send_email():
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    
    # Compose the email message
    subject = 'Anomaly Detected in API Requests'
    body = 'An anomaly has been detected in the API requests. Please check the dashboard.'
    message = f'Subject: {subject}\n\n{body}'
    
    # Send the email
    server.sendmail('your-email@gmail.com', 'registered-email@example.com', message)
    
    # Close the SMTP server
    server.quit()

def main():
    current_requests = make_api_call()
    if detect_anomaly(current_requests):
        send_email()