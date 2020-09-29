# student-management-system
A complete Django API project to add and manage schools and students using Django-Rest-Framework.

This project consists of the following two tables.

* Student
* School

School is the foreign key to the student table. Since this is a sample project I am using the default sqlite3 database 
for the database.

You can add/view/edit/delete students and schools.

## Installation

Clone the repo and run

```pip install -r requirements.txt```

This will install all the required packages and libraries.
 
 After that run
 
```console
terminal:~$ python manage.py migrations
```

This will create a migrations folder in the current directory, which consists of SQL statements and queries.

```console
terminal:~$ python maage.py migrate
```

This will apply the migrations( Execute the SQL statements and make the db changes)



 