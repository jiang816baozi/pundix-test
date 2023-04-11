# report/html_report.py

from jinja2 import Environment, FileSystemLoader

def generate_html_report(result):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("report_template.html")

    with open("report.html", "w") as f:
        f.write(template.render(result=result))
