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
* [uv](https://docs.astral.sh/uv/getting-started/installation/) - an extremely fast Python package and project manager

### Set-Up
Clone the repository:
```bash
git clone https://github.com/rafaljab/apiAutomationPlayground.git
```
If you want more freedom, you can fork the repository first instead of cloning it directly.

Instead of cloning/forking the repository, you can download the release of your choice. 
Just go to the [selected release](https://github.com/rafaljab/apiAutomationPlayground/releases), 
and download a zip file with source code. Then, unzip the file to the desired location.

Go to the project directory:
```bash
cd apiAutomationPlayground
```

Instead of using standard `pip` and `venv`, this project uses `uv` for dependency management. If you don't have `uv` installed, [install it first](https://docs.astral.sh/uv/getting-started/installation/) (e.g. `pip install uv` or `Invoke-WebRequest -Uri https://astral.sh/uv/install.ps1 -OutFile uv-install.ps1; .\uv-install.ps1`).

Now, ask `uv` to automatically create a virtual environment and install all dependencies:
```bash
uv sync --all-groups
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
uv run manage.py runserver
```
Open your web browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

**B) Using CMD Script (Windows)**

Just open the `start-app.cmd` file. It will run the above command for you.

## Tests
This repository also contains API tests (using Pytest) - see `shop/tests.py` for an example.
You can run them using:
```bash
uv run pytest
```

You can find end-to-end automated tests in separate repositories:
- [helloPlaywrightPy](https://github.com/rafaljab/helloPlaywrightPy) - Playwright with Python
- [hello-playwright-ts](https://github.com/rafaljab/hello-playwright-ts) - Playwright with Typescript
