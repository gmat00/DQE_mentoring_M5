# DQE Mentoring - Module 4 - PyTest

## Create a DB on you\'r local MS SQL Server
Open and run the next sql query to create DataBase, 2 schemas and fill-in basic data.
```
CREATE DATABASE AdventureWorks2012

USE AdventureWorks2012

CREATE SCHEMA Person

USE SCHEMA Person

CREATE TABLE [Person].[Address] ( AddressID INT PRIMARY KEY, Address VARCHAR(100), City VARCHAR(50), StateProvince VARCHAR(50), PostalCode VARCHAR(20), CountryRegion VARCHAR(50) );

CREATE SCHEMA Production

CREATE TABLE [Production].[Document] ( DocumentID INT PRIMARY KEY, DocumentNumber VARCHAR(50), Title VARCHAR(100));

CREATE TABLE [Production].[UnitMeasure] ( UnitMeasureCode VARCHAR(10) PRIMARY KEY, Name VARCHAR(50));

INSERT INTO [Person].[Address] (AddressID, Address, City, StateProvince, PostalCode, CountryRegion) VALUES (1, '123 Main Street', 'New York', 'NY', '10001', 'USA'), (2, '456 Elm Street 1', 'Los Angeles', 'CA', '90001', 'USA'), (3, '789 Oak Avenue', 'Chicago', 'IL', '60007', 'USA');

INSERT INTO [Production].[Document] (DocumentID, DocumentNumber, Title) VALUES (1, 'DOC001', 'sales_report.docx'), (2, 'DOC002', 'marketing_plan.docx'), (3, 'DOC003', 'operations_manual.docx');

INSERT INTO [Production].[UnitMeasure] (UnitMeasureCode, Name) VALUES ('M', 'Meter'), ('KG', 'Kilogram'), ('EA', 'Each');

SELECT * FROM [Person].[Address]

SELECT * FROM [Production].[Document]
```

## Generate a User for establishing connection between PyTest and DB
Fill in Login name, Password and User name in the next script and run the query:
```
CREATE LOGIN <Login Name> WITH PASSWORD = '<Password>';

CREATE USER <User Name> FOR LOGIN <Login Name>;

GRANT CONNECT SQL TO <User Name>;
```

Now DB is ready for the next steps.
***

# Preparations to run the PyTest project

- [ ] Download git repository
- [ ] Open the project
- [ ] Install pip
``` 
Windows: py -m ensurepip --upgrade
Linux/Mac: python -m ensurepip --upgrade
```
- [ ] Install PyTest
```
pip install -U pytest
```
- [ ] Install PyODBC
```
pip install pyodbc
```
### Change config parameters in accordance with your local MS SQL Server configuration
- [ ] Fill in value of SERVER variable 
- [ ] Fill in value of DATABASE variable 
- [ ] Fill in value of USERNAME variable (if needed)
- [ ] Fill in value of PASSWORD variable (if needed)
### In case if connection to your MS SQL Server requires login and password change authorisation request in the app.connect_to_db function !

## Run the PyTest with generating html-report
run next command in the console/terminal: 
```
py -m pytest '.\dqe_mentoring\test.py' --html=report.html
```

***
# Helpful links:
- Python SQL Driver https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16
- PyTest https://realpython.com/pytest-python-testing/
- PyTest and SQL https://itnext.io/setting-up-transactional-tests-with-pytest-and-sqlalchemy-b2d726347629
- SQL Connection https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver16
- SQL Create User https://www.tutorialspoint.com/ms_sql_server/ms_sql_server_create_users.htm
