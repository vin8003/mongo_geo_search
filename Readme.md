This is a example of geospatial search in MongoDB using pymongo

It is recommended to always work in a virtual environment (i personally prefer to use virtualenv)
lets create a virtual environment in python3 using virtualenv wrapper
open a terminal and make sure you have virtualenv and mongodb up and running

$virtualenv -p python3 /path/to/your/env

Now activate the environment you just created

$source /path/to/your/env/bin/activate

Install the dependencies

$pip install -r requirements.txt
(or you can just pip install pymongo)

you can upload the sample uncleaned data into the database using mongo_insert_example.py


The geospatial search uses a special geospatial index in order to search according to cordinated. It requires a
predetermined order of the data in order to make a geospatial search. The data should be in a list or tuple
containing only the float value of the coordinates in the form of (x, y) or [x, y]

Now we have the data in the format - {'distid': 47, 'state': 'UP', 'gps': '25.4484° N, 78.5685° E', 'distname': 'Jhansi'}
but we need it in this format - {'distid': 47, 'state': 'UP', 'gps': [25.4484, 78.5685], 'distname': 'Jhansi'}

so by running the cordinate_cleaner.py, we can remove the degree sign by using regualar expressions and reorganize
the whole data and store it a file (for later importing to the database) or we can directly store it in mongodb

Now we can run geospatial_search.py and let it build the index table for the first time, then we can change the loc
parameter and it will search according to the coordinates