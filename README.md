
## Overview

The ``pack`` package is a pip installable package that takes a user query as a funciton call and 
outputs the top 10 works relevant to the specified field id with the greatest number of citations.

Additionally, heatmaps are generated showing the frequency of the top publishers and intitutions 
that have works matching the users query. This visiualizations serves to aid the user in further
literature exploration.

---

Installation
---
``pip install .`` in Package-root


Usage
---

After installing the package and importing all files, the following commands will be available 

- ``FieldInfo`` class object that returns summary information on fields 
- ``SibInfo`` class object that returns summary information on related fields and takes as input a 
field id
- ``work_search(query,id)`` function that takes a query and field id and provides a tabulated 
summary and heat map visualizaitons



## 📂 Repository Structure

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

After installing this package...
