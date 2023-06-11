# Automation framework
Automation framework to API, WEB and MOBILE tests.

---
### Project installation

1 - Clone repository.

2 - Create Python interpreter.

3 - Install requirements.

4 - Configurate environment variables to Allure-Report:

    (source: https://scoop.sh/). In Windows PowerShell console send:
    
    > Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    
    > irm get.scoop.sh | iex
    
    > scoop install allure

---
### Commands to run tests:  
- Run **all** test suite:
    > pytest

- Run tests with the **tag** (e.g: pytest -m SMOKE):
    > pytest **-m** {**tag**}

- Run tests of a **class** or containing the test **name** (e.g: pytest -k TestLogin):
    > pytest **-k** {**className** or **testName**}

---
### Open Allure report
Command to open Allure report:

> allure serve + ***.allure-report path***

For example:

>allure serve C:\path\.allure-report

>allure serve .allure-report