# righter

Python scripts for identifying common English writing mistakes


## How to get the dataset

Go to

    https://corpus.mml.cam.ac.uk/efcamdat1/access.php

Create an account and go to select scripts. Select all data you want exported.
Then navigate to export data and make sure the following options are marked
(and none other):

    - Selected scripts
    - Error corrections
    - XML uncompressed

Click "Export data" and then on the link to download.

The downloaded XML is not ready for being processed, as it contains a few
errors. In order to fix the known issues run the script fix-xml inside scripts.
Eg.:

    $ scripts/fix-xml EF20130315_selection299.xml

This will correct the XML file in-place. Now the XML file is ready for being
further processed.


## How to use

After having fixed the XML, it is possible to export it to a list of JSONs:

```
    PYTHONPATH=src python -m righter.parser data/EF20130315_selection299.xml data/299.txt
```

This is an example of implementation to identify English mistakes (feel free to implement your own :)):
```
    PYTHONPATH=src:$PYTHONPATH python -m righter.predict -i data/299.txt -o data/299-predictions.txt
```

In order to see its precision and recall, it is possible to use:
```
    PYTHONPATH=src:$PYTHONPATH python -m righter.analyse -i data/299.txt -p data/299.txt  --mistake-type C
```

In order to generate plots on annotated data

```
    PYTHONPATH=src python -m righter.plot -i 299.txt
```

Notice that matplotlib must be installed for this to run. By default it will
generate a graph with the top 10 most common errors
