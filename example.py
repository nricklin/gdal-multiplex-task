from gbdxtools import Interface
gbdx = Interface()

task = gbdx.Task('gdal-cli-multiplex')
task.inputs.data1 = 's3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/test_acomp_output/'
task.inputs.data2 = 's3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/test_acomp_output/'

task.inputs.command = """
gdalbuildvrt $outdir/out.vrt $indir/data1/*.tif $indir/data2/*.tif;
gdal_translate $outdir/out.vrt $outdir/out.tif;
ls $indir/data1/ > $outdir/list1.txt;
ls $indir/data2/ > $outdir/list2.txt
"""

workflow = gbdx.Workflow([task])
workflow.savedata(task.outputs.data, location='gdal-multiplex-task-output')
workflow.execute()