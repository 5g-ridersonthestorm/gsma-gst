# TOSCA

The contents of this directory contain TOSCA templates which can be used as a data driven method of specifying the translation from service instance request to resource instance requests.

There are two sets of files:

## Assured connection
5G_datatypes.yml will hold the GST in TOSCA format
5G.yml will hold a template for the overall 5G service and will include the file above
5G Service Assure.yml assigns specific values to the variables defined in the file above in order to define the required 5G service instance. Thus it is TOSCA version of NEST.

## MEC Hosting
mec_hosting_set_up.yml is run when the service is first ordered. One of its functions is to dynamically create a TOSCA template ready for use when the MEC hosting is to be enabled. It does this by requiring a run of the program create_enablement_tosca.py. That python program takes the values originally submitted in mec_hosting_set_up_inputs.yml and uses them to render the jinja2 template mec_hosting_enablement.j2
An example of such a dyanmically created template is mec_hosting_enablementwheresmychargepoint.com.yml