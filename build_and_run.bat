@echo off

:: Create the virtual environment
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
if exist requirements.txt (
    pip install -r requirements.txt
)

:: Run the program
python src\main.py
