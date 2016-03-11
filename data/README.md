#External files

## Valid English words

These files were copied from the Debian package `scowl 7.1-1` (663.016 words):
- british-english-insane
- american-english-insane


## Abbreviations

This list of abbreviations was originally retrieved from:
http://www.aresearchguide.com/comabb.html

http://www.acronymfinder.com/

## List of names

In order to extract a list of names from our annotated base I did the following
modification. The resulted list is in data/names.txt
diff --git a/src/righter/analyse.py b/src/righter/analyse.py
index ddcac8a..66c4448 100644
--- a/src/righter/analyse.py
+++ b/src/righter/analyse.py
@@ -1,4 +1,7 @@
 import argparse
+import string
+import collections
+import random
 import json
 from statistics import mean, stdev
 import textwrap
@@ -46,7 +49,7 @@ def format_text(text):
 
 def show_qualitative(baseline, predicted):
     data = []
-    
+
     baseline_dict = map_id_to_field(baseline, "changes")
     predicted_dict = map_id_to_field(predicted, "changes")
     writings_dict = map_id_to_field(baseline, "text")
@@ -124,13 +127,30 @@ if __name__ == "__main__":
     parser.add_argument('-o', '--file-output', help='Save analysis to output file')
     args = parser.parse_args()
 
-    annotated = read_writings(args.annotated_file, args.mistake_type)
-    predicted = read_writings(args.predicted_file, args.mistake_type)
-    if args.analysis_type in ["all", "qualitative"]:
-        print("\nDetailed comparison")
-        show_qualitative(annotated, predicted)
-
-    if args.analysis_type in ["all", 'quantitative']:
-        print("\nSummary")
-        show_quantitative(annotated, predicted)
+    annotated = map_id_to_field(read_writings(args.annotated_file, args.mistake_type), 'changes')
+    predicted = map_id_to_field(read_writings(args.predicted_file, args.mistake_type), 'changes')
+    keys = list(predicted.keys())
+    random.shuffle(keys)
+    count = collections.defaultdict(lambda: 0)
+    for key in keys[:130000]:
+        selections = set()
+        for change in annotated.get(key, []):
+            selections.add(change['selection'])
+        for change in predicted.get(key, []):
+            selection = change['selection']
+            if selection not in selections and selection[0] in string.ascii_uppercase:
+                count[selection] += 1
+    items = list(count.items())
+    items.sort(key=lambda x: x[1])
+    for key, c in items:
+        if c >= 3:
+            print(key)
+
+    #if args.analysis_type in ["all", "qualitative"]:
+    #    print("\nDetailed comparison")
+    #    show_qualitative(annotated, predicted)
+
+    #if args.analysis_type in ["all", 'quantitative']:
+    #    print("\nSummary")
+    #    show_quantitative(annotated, predicted)
 
