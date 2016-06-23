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