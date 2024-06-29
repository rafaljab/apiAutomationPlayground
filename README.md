# API Automation Playground
That is a simple web application based on Django Rest Framework for playing with a test automation framework.

## Live Demo
**Open the link: [https://apiautomationplayground.pythonanywhere.com/api/shop/products/](https://apiautomationplayground.pythonanywhere.com/api/shop/products/)**

Additionally, you can check out the React application [GUI Automation Playground](https://rafaljab.github.io/gui-automation-playground), 
which partially uses endpoints from this backend. Its GitHub repository is available here: 
https://github.com/rafaljab/gui-automation-playground.

## Endpoints
* Shop
    * Products view - [/api/shop/products/](https://apiautomationplayground.pythonanywhere.com/api/shop/products/)
    * Product view - [/api/shop/products/$productId/](https://apiautomationplayground.pythonanywhere.com/api/shop/products/1/)

## Usage
For your test automation practice, you can:
* use a deployed application (the latest release) that is available online - link to live demo above, or
* clone the repository and run the application in dev-mode (recent changes; if you synchronize the repository in the future, you'll probably have to adjust the tests), or
* if you need a stable application, download a zip package with a specific release and run it locally in dev-mode.

### Dependencies
* [Python](https://www.python.org/) (I use version 3.12.3, but you can probably use a newer version too)

### Set-Up
Clone the repository:
```bash
git clone https://github.com/rafaljab/apiAutomationPlayground.git
```
If you want more freedom, you can fork the repository first instead of cloning it directly.

Instead of cloning/forking the repository, you can download the release of your choice. 
Just go to the [selected release](https://github.com/rafaljab/apiAutomationPlayground/releases), 
and download a zip file with source code. Then, unzip the file to the desired location.

Then you need to create a virtual environment. If you don't have virtualenv package installed on your machine, 
you need to run this command first:
```bash
pip install virtualenv
```

Now, you can create and activate a new virtual environment, but first, go to the main catalog:
```bash
cd apiAutomationPlayground
python -m venv .venv
.\.venv\Scripts\activate
```

The above instructions work for Windows (Powershell). If you have Unix/macOS or want to learn more 
about virtual environments, here's the official documentation: 
[Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Now, when you've activated the virtual environment, install all required packages in it:
```bash
pip install -r requirements/base.txt
```

Create an `.env` file in the root directory (apiAutomationPlayground). 
This file is ignored by Git. Sample file content is in the `.env.dist` file. 
Replace secret key with your random value. (You can use https://djecrety.ir/ for this.)

You're all set!

### Run App Locally
You can start the application manually (A) or by using a ready-made CMD script (B).

**A) Manually**

Run the following command to start the application (dev mode):
```bash
.\.venv\Scripts\activate
python manage.py runserver
```
Open your web browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

**B) Using CMD Script (Windows)**

Just open the `start-app.cmd` file. It will run above commands for you.

## Tests
This repository also contains API tests (using Pytest) - see `shop/tests.py` for an example.

You can find end-to-end automated tests in separate repositories:
- [helloPlaywrightPy](https://github.com/rafaljab/helloPlaywrightPy) - Playwright with Python
- [hello-playwright-ts](https://github.com/rafaljab/hello-playwright-ts) - Playwright with Typescript
