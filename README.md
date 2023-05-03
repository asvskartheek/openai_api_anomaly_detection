# OpenAI Anomaly Detector & Email Trigger
This repo analyzes the latest data, and detects any anomalies (if found). If an anomaly is detected, it sends an email to a registered email address. Also, provided with a very handy file deploy_to_aws_lambda.py to run this on your own at absolutely fraction of a cost.

## Pipeline
- [] Provide maintainance and hosting of this.
- [] Select custom Anomaly detection algorithms
- [] Plug & Play their own Anomaly detection algorithms

## Support Me
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/asvs)
## Getting Started
To use this script, you will need the following:
1. A database to store the timeseries data. You can use any database of your choice like MySQL, PostgreSQL, SQLite, etc.
2. A registered email address to receive alerts.

## Setup
1. Dev Setup 
```bash
git clone https://github.com/your-username/api-request-anomaly-detector.git
python -m venv venv
source venv/bin/activate
pip install requests pandas sqlite3 smtplib
```
2. Edit the config.py file to set the following variables:
3. Deploy to AWS Lambda
```python
python deploy_to_aws_lambda.py
```

**THAT'S IT!**

The script will start pinging the API endpoint every 6 minutes and storing the data in the database. If an anomaly is detected, it will send an email to the registered email address.

## Contributing
If you find a bug or want to contribute to this project, please create a pull request or submit an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.