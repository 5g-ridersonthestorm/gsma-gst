import jinja2
import sys
import os




# get arguments and set them in 
# TODO get args using getopt and put them into render_vars instead of the hard code example below 
render_vars = {
    "app_image_file": "string from arg for image_file" 
    "app_state_data": "string from arg for state" 
    "app_public_url": "string from arg for url" 
}

template_filename = "mec_hosting_enablement.j2"
rendered_filename = "mec_hosting_enablement"+app_public_url+"".yml"

script_path = os.path.dirname(os.path.abspath(__file__))
template_file_path = os.path.join(current_path, template_filename)
rendered_file_path = os.path.join(current_path, rendered_filename)

# set render env
render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_file_path))
# render arguments into the jinja2 template
output_text = environment.get_template(template_filename).render(render_vars)
# write the result 
with open(rendered_file_path, "w") as result_file:
    result_file.write(output_text)