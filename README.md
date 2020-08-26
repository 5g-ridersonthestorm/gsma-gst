# gsma-gst
Work on GSMA GSTs

The Generic Network Slice Template (GST) is a set of attributes that can characterise a type of network slice/service. GST is generic and is not tied to any specific network deployment.
The NEtwork Slice Type (NEST) is a GST filled with values. The values are assigned to express a given set of requirements to support a network slice customer use case. The NEST is an input to the network slice preparation performed by the Network Slice Provider (NSP). 


Generic Network Slice Template
Version 3.0
22 May 2020
https://www.gsma.com/newsroom/wp-content/uploads//NG.116-v3.0.pdf


| Term                          | Description                                                                                                                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Network Slice                 | A logical network that provides specific network capabilities and network characteristics                                                                                                |
| Network Slice Instance        | A set of Network Function instances and the required resources (e.g. compute, storage and networking resources) which form a deployed Network Slice as defined in section 3.1 of         |
| Network Slice Subnet          | A representation of the management aspects of a set of Managed Functions and the required resources (e.g. compute, storage and networking resources)                                   |
| Network Slice Subnet Instance | An instance of Network Slice Subnet representing the management aspects of a set of Managed Function instances and the used resources (e.g. compute, storage and networking resources)  |
| Service Continuity            | The uninterrupted user experience of a service, including the cases of IP address and/or anchoring point change                                                                   |
<p align="center"><img src="https://github.com/5g-ridersonthestorm/gsma-gst/wiki/images/gsma-nest-thinking.png" /></p>

This repository contains

# Organization of this repository

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
+---gst
|   |   generic-slice-template.xlsx
|   |   
|   \---json-schema
|           1-who.json
|           2-what.json
|           3-where.json
|           4-when.json
|           5-traffic-profile.json
|           6-device-profile.json
|           7-common-properties.json
|           8-data-access-profile.json
|           9-mobility-profile.json
|           10-v-2-x-profile.json
|           11-ue-positioning-profile.json
|           12-deterministic-comms-profile.json
|           13-mission-critical-profile.json
|           14-commercial-profile.json
|           15-operational-profile.json
|           16-third-party-network-and-application-functions.json
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

## Developing Templates

templates are captured in excel format and then JSON schema and JSON examples are generated


### JSON Schema
JSON Schema describes JSON data. It’s like a database schema for JSON and can be used to validate a JSON instance before it’s sent to an API.

Here is an example schema for a part of generic slice template

```json  
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "WHAT",
    "description": "WHAT",
    "type": "object",
    "properties": {
        "WhatsDrivingTheConnectivityRequirement?": {
            "description": "Connectivity requirement in plain text",
            "type": "string"
        },
        "UseCaseType": {
            "description": "Use case, per NGMN",
            "type": "string"
        },
        "Service/SliceType(Sst)": {
            "description": "Service/Slice Type",
            "type": "string",
            "enum": [
                "eMBB",
                "uRLLC",
                "mMTC"
            ],
            "minItems": "1"
        },
        "SliceDifferentiator": {
            "description": "Slice differentiator  ",
            "type": "string"
        },
        "NumberOfTerminals": {
            "description": "Number of terminals or UEs",
            "type": "string",
            "maxLength": "22"
        },
        "NumberOfConnections": {
            "description": "Number of connections.  If not populated,  assumed to be same as number of Ues",
            "type": "string"
        }
    },
    "required": [
        "NumberOfTerminals"
    ]
}
```

And here is JSON data that matches that schema.
```json
{
    "WhatsDrivingTheConnectivityRequirement?": "Collect wearable sensor data",
    "UseCaseType": "Smart wearables ",
    "Service/SliceType(Sst)": "mIOT",
    "SliceDifferentiator": "example",
    "NumberOfTerminals": "200000",
    "NumberOfConnections": "200000"
}
```


Let’s go through each property in the schema

_type_

The type attribute describes the data type such as string, object or number. You can find the whole list here. Each type has its own set of validation keywords that make up the rest of the schema. We’ll describe two validation keywords below.

_properties_

The properties attribute is validation keyword for JSON objects. This properties object defines each valid property along with an additional level of validation schema. If one of the properties is an object, you can continue to nest that representation as deep as necessary.

_required_

The required attribute is another validation keyword specific to objects. The value of required should be an array of strings, where each string is a key in the properties object. JSON data is not valid against this schema if any of the properties in the required array are missing.

So using the example above, the following JSON data is valid because the title and body are optional
```json
{
    "NumberOfTerminals": "200000"
}
```
And this JSON data is not valid because NumberOfTerminals is required
```json
{
    "Service/SliceType(Sst)": "eMBB",
    "SliceDifferentiator": "D143A5"
}
```
Once your API consumers have a JSON schema, they can use one of the many JSON Schema libraries to validate their JSON data.

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

