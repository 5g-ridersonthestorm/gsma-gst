import jinja2
import sys
import os
import json

# command line for use: python create_enablement_tosca.py '{"app_image_file": "http://cloudrepo:80/files/wheresmychargepointapp.iso","app_state_data": "data_url.com","app_public_url": "wheresmychargepointapp.com"}'
# command line for use: python create_enablement_tosca.py '{"app_image_file": "http://cloudrepo:80/files/test.iso","app_state_data": "data_url.com","app_public_url": "test.com"}'

# get arguments and set to render
render_vars = json.loads(sys.argv[1])

template_filename = "mec_hosting_enablement.j2"
rendered_filename = "mec_hosting_enablement"+render_vars.get("app_public_url")+".yml"

script_path = os.path.dirname(os.path.abspath(__file__))
template_file_path = os.path.join(os.curdir, template_filename)
rendered_file_path = os.path.join(script_path, rendered_filename)


# set render env
render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
# render arguments into the jinja2 template
output_text = render_environment.get_template(template_filename).render(render_vars)
# write the result 
with open(rendered_file_path, "w") as result_file:
    result_file.write(output_text)