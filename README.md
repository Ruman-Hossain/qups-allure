# qups-allure
## Required Tools and Technologies
* Python Installed in your pc
* Pip
* allure
* Selenium Web Driver
* Editor ( VS Code / Sublime / PyCharm). I prefer PyCharm

## Virtual Environment Setup
Lets create an isolated environment for "Whatsapp ui automation" project to install required library packages so that we can use it.
### PyCharm Environment Setup
Using PyCharm this is quite easier. While creating a new project this will ask you to Create Virtual Enviroment

### VS Code Environment Setup


> Step-1: Create Virtual Environment
```shell
    python -m venv venv

```
> Step-2: Activate the Virtual Env
```shell
    .\venv\Scripts\activate

```
> Step-3: Install Required Library from the *requirements.txt* File
```shell
    pip install -r requirements.txt

```
> Step-4 : Run and Test the Script 
```shell
    python example.py
```
> Step-5: Now Follow the Instructions Shown in Screen. After Successfull running of the script you will get the test Results in Excel file.

## Required Library Packages Installation
### Pycharm
Go to 
* File 
    - Settings
      - Project:WhatsAppUIAutomation
        - Python Interpreter  (Select Python Interpreter if not auto selected)
        - Install Required Packages Clicking (+) install sign
### Installation Using command line
```shell
    pip install -r requirements.txt
```

## Project Code Explanation