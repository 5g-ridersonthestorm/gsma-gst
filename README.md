# gsma-gst
Work on GSMA GSTs

<p align="center"><img src="https://github.com/5g-ridersonthestorm/gsma-gst/wiki/images/gsma-nest-thinking.png" /></p>

This repository contains

# Organization of the repository

* gst: contains the generic slice template (template only, no slice details) 
* s-nest: contains examples of the Standardized NESTs per industry vertical
* p-nest:  contains examples of the Private NESTs per operator/vendor.

This is the tree structure of the repository:

```
Folder PATH listing for volume DATA
Volume serial number is 0003-6809
D:.
|   gsma-gst.iml
|   LICENSE
|   README.md
|   SliceTemplateBlueprint.xlsm
|   
+---.idea
|   |   misc.xml
|   |   modules.xml
|   |   sonarIssues.xml
|   |   vcs.xml
|   |   workspace.xml
|   |   
|   \---inspectionProfiles
|           Project_Default.xml
|           
+---gst
|   |   generic-slice-template.xlsx
|   |   
|   \---json-schema
|           1-who.json
|           10-v-2-x-profile.json
|           11-ue-positioning-profile.json
|           12-deterministic-comms-profile.json
|           13-mission-critical-profile.json
|           14-commercial-profile.json
|           15-operational-profile.json
|           16-third-party-network-and-application-functions.json
|           2-what.json
|           3-where.json
|           4-when.json
|           5-traffic-profile.json
|           6-device-profile.json
|           7-common-properties.json
|           8-data-access-profile.json
|           9-mobility-profile.json
|           
+---p-nest
|       example-p-nest.yaml
|       
\---s-nest
    |   readme.txt
    |   
    \---collect-wearable-sensor-data
        +---example
        |       commercial-profile.json
        |       common-properties.json
        |       data-access-profile.json
        |       deterministic-comms-profile.json
        |       device-profile.json
        |       mission-critical-profile.json
        |       mobility-profile.json
        |       operational-profile.json
        |       third-party-network-and-application-functions.json
        |       traffic-profile.json
        |       ue-positioning-profile.json
        |       v-2-x-profile.json
        |       what.json
        |       when.json
        |       where.json
        |       who.json
        |       
        \---schema
                commercial-profile.json
                common-properties.json
                data-access-profile.json
                deterministic-comms-profile.json
                device-profile.json
                mission-critical-profile.json
                mobility-profile.json
                operational-profile.json
                third-party-network-and-application-functions.json
                traffic-profile.json
                ue-positioning-profile.json
                v-2-x-profile.json
                what.json
                when.json
                where.json
                who.json
                

```

## Developing

templates are captured in excel format and then JSON schema and JSON examples are generated

### Prerequisites


## Setting up environment

Here's a brief intro about what a developer must do in order to generate templates

```
git clone https://github.com/5g-ridersonthestorm/gsma-gst.git
cd gsma-gst/
```

## Usage


## Contributing

To contribute to the development of the project you have to fork the repository, commit new code and create pull requests.

## Licensing

This repository is under Apache 2.0 License

## Lead Developer

* [@kweveen](https://github.com/kweveen) Kevin McDonnell

