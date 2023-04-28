
# Food Menu App
___

This is a web application built on the Django framework that provides user authentication functionality, as well as basic CRUD operations for managing food items. Users can perform Create, Read, Update, and Delete (CRUD) operations on food items.

## Requirements
___

The application requries the following to run:

* Python 3.10
* Django 3.2

## Usage

### Setup
___

Before running the app, a superuser must be created to access the admin functionalites that django provides. A superuser can be created using the below command, it will prompt the user to enter a username and password which are later used to login to the admin site of the application.

```bash
python manage.py createsuperuser
```

Once the superuser is created, the application can run normally.

### Running the Application
___

To run the application, use the below command:

```bash
python manage.py runserver
```

Once the application is running, go to localhost:8000.



