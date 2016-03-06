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
