# web_ui_testing

**Running Tests**

* On Pycharm Terminal, change directory into:

`~\web_ui_testing`

* On Pycharm Terminal, execute:

`pipenv run python -m pytest tests/<test to run>`

**Configuration**

On `~\web_ui_testing\tests\config.json` select "chrome" or "firefox" to define browser

**Reports**

Reports are automatically created on `~\web_ui_testing\Reports\Report.html`
To configure reports location, or disable reporting, change configurations on `~\web_ui_testing\pytest.ini`
