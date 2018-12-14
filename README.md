# ABCWarehouse Alarm Client software
Python 3.7.1, PyInstaller 3.3.1, Plyer 1.3.2, Django 1.8, SQLite 
C# .NET Windows Form App
Ubuntu Shell

This project is to develop alarm software running on cross-platform (mainly tested on Windows 10, Ubuntu).
1. Alarm client have a api to be called by server software. The api will notify as system notification and save received alarm on db.
2. Alarm should have UI to show alarm list. It have scroll. Currently the UI is implemented by Django web app. 
3. Alarm client will have controller or manager.