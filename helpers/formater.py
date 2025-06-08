from jinja2 import Environment, FileSystemLoader
import os

class XMLTemplateRenderer:
    def __init__(self, template_path):
        self.template_path = template_path
        abs_template_path = os.path.abspath(template_path)
        self.env = Environment(
            loader=FileSystemLoader(os.path.dirname(abs_template_path))
        )
        self.template_name = os.path.basename(template_path)

    def render(self, context):
        template = self.env.get_template(self.template_name)
        return template.render(context)