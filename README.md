# gdal-gbdx-task
A docker GBDX task for doing arbitrary gdal operations on data within DigitalGlobe's GBDX platform


Intended to use with gbdxtools like this:

```python
from gbdxtools import Interface
gbdx = Interface()

task = gbdx.Task('gdal-cli-multiplex')
task.inputs.data1 = 's3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/test_acomp_output/'
task.inputs.data2 = 's3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/test_acomp_output/'

task.inputs.command = """
ls $indir/data1/ > $outdir/list1.txt;
ls $indir/data2/ > $outdir/list2.txt
"""

workflow = gbdx.Workflow([task])
workflow.savedata(task.outputs.data, location='gdal-multiplex-task-output')
workflow.execute()
```


Current Substitutions:

* $input - absolute input path to a file found
* $output - absolute output path to be written (filename is the same as input filename)

More Substitutions we could use:

* $output_directory
* $output_filename
* $output_file_no_extension
* $output_file_extension
