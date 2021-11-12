# Evreka Database implementetion trials
## First qustionaire for the implementation of foreign key accesing
For the implementation of the first database model seperate two classes namely Vehicle and Navigation Record created. Within reach of two classes a foreign key field is implemented over the Navigation Record class.

For the query request of the whole database a get method is implemented to view the records. Such implementation is modified to be in reach of needed format of the data.

Since the model suggests a two class system the implementation is verified over the whole data to particular records.

### Suggestion for an alternative construct
A database on csv base can be implemented and analyzed. A live data stream can be buffered into a csv format and the strength of modules like pandas on python or Shiny for R can be achieved. Also such a database system may give power to the machine-learning applications on ready to use.

## Second questionaire for the implementation
This part includes a pair check display for the output of the query method. The similar method is used with respect to previous part with a validation over the ids of the Bins and the operations. Such system is implemented in a method base query.

### Notes:
Check the system by manage.py shell by.
```
$ python manage.py shell
```
and then import relevant modules.
For the first project in evrekadb,
```python
>>> from query.models import NavigationRecord, Vehicle, get_last_point
>>> get_last_point()
```
For the second project in evrekadb2,
```python
>>> from query.models import Bin, Operation, get_freqs
>>> get_freqs(idb=43523, ido=1234)
```

Note that the second project query suggest an id base query where it is checked with prefilled data. So such a query should be made for relevant id pairs for bin and operations.