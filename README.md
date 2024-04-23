
---

## Overview

The ``pack`` package is a pip installable package that takes a user query as a funciton call and 
outputs the top 10 works relevant to the specified field id with the greatest number of citations.

Additionally, heatmaps are generated showing the frequency of the top 15 publishers, intitutions,
and first-named authors that have works matching the users query. These visiualizations serve to aid the user 
in further literature exploration.

---

## Repository Structure


```sh
├── LICENSE
├── pack
│   ├── __init__.py
│   ├── main.py
│   ├── test_search_function.py
│   └── utils
│       ├── fields.py
│       ├── heatmap.py
│       ├── __init__.py
│       ├── siblings.py
│       └── tests.py
├── README.md
└── setup.py
```

---

## Installation

``pip install .`` in Package-root

---

## Usage


After installing the package and importing all files, the following commands will be available 

- ``FieldInfo`` class object that returns summary information on fields 
- ``SibInfo`` class object that returns summary information on related fields and takes as input a 
field id
- ``work_search(query,id)`` function that takes a query and field id and provides a tabulated 
summary and heat map visualizaitons

Typical usage scenarios include running the following in a notebook:
    
    FieldInfo().field_info() --> returns printed summary of all fields
    SibInfo(15).sib_info() --> returns printed summary of all subfields for field id=15
    work_search('redox flow battery',15) --> returns summary of top 10 works and heat maps 
                                              of top 15 journals, institutions, and authors.
        
Additional information on each function and class can be found in their docstrings.

---

## Author
[Abdul Ahmed](https://github.com/a0ahmed)
