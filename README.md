# How to Run the Project

Follow these steps to run this Django project on your machine.

## 1. **Clone the repository**

`git clone https://github.com/phpc99/django-project2.git `
`cd django-project2` 

## 2. **Create a virtual environment**

`python -m venv venv` 

## 3. **Activate the virtual environment**

### Windows (PowerShell or CMD):

`venv\Scripts\activate` 

### macOS / Linux:

`source venv/bin/activate` 

You should now see `(venv)` at the start of your terminal prompt.

## 4. **Install dependencies**

`pip install -r requirements.txt` 

## 5. **Apply migrations**

`python manage.py migrate` 

## 6. **Run the development server**

`python manage.py runserver` 

## 7. **Open the website**

Go to: http://127.0.0.1:8000/
