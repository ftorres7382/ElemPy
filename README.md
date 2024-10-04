# ElemPy

## Description


## Files

## How To Contribute (In Progress)
1. All pull requests will be reviewed/changed/approved only by the core team
1. Implement code based on functionality, one funtionality = one pull (the more basic, the easier it is to approve)
1. Implement classes in **packages/custom_types.py** if you need special types to help with parameter validation
1. Functions that will be used by parts of the main program should take in python or 3rd party package types as input. It should then handle the standardization using custom types. All custom types implemented will be for the internals of the packages or internals of routes only.
    - Example: function that sends an email should accept a python string type and convert it to a custom email type to validate the email (these types can be imported using 3rd party tools)
1. All function definitions and parameters must have type annotations and return types which will be strictly checked in runtime using mypy. This helps with collaboration
    - It needs to pass the mypy --strict check