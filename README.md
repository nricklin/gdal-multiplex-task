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
mkdir $outdir/data_out1  # create output multiplex port
mkdir $outdir/data_out2  # create output multiplex port
ls $indir/data1/ > $outdir/data_out1/list1.txt;
ls $indir/data2/ > $outdir/data_out2/list2.txt
"""

workflow = gbdx.Workflow([task])
workflow.savedata(task.outputs.data_out1, location='gdal-multiplex-task-output/out1')
workflow.savedata(task.outputs.data_out2, location='gdal-multiplex-task-output/out2')
workflow.execute()
```


Current Substitutions:

* $indir - path to where the input port directory will be
* $outdir - path to where the output port directory will be

More Substitutions we could use:

* $output_directory
* $output_filename
* $output_file_no_extension
* $output_file_extension
