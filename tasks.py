from invoke import task

@task
def run_dev(c):
    c.run("python -m pytest tests/ --env=dev --alluredir=reports/allure")

@task
def report(c):
    c.run("allure serve reports/allure")