# wifi_lma

BRC Info website utilizing [Wagtail](https://wagtail.org/).

## Installation

1. Download the code from the from the [github repository](https://github.com/LCBRU/wifi_lma).
2. CD into the project directory
3. Create a virtual environment: `python3 -m venv venv`
4. Enable the virtual environment: `. ./venv/bin/activate`
5. Install the requirements: `pip install -r requirements.txt`
6. Create the database: `python manage.py migrate`
7. Create a super user: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`
9. View the website at [http://localhost:8000](http://localhost:8000)
10. Edit the website at [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Deployment

1. Collect static files using the command `python manage.py collectstatic`
2. Check into github
3. Download onto the server
4. Copy the `example.env` file to `.env` and fill the variables.