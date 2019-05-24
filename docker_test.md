For testing that the Docker container behaves as expected before deploying as a GBDX Task:

Set LOCAL_PATH env var
`LOCAL_PATH=$(pwd)`

To test a command that should succeed:
`docker run --rm -v $LOCAL_PATH/sample_input:/mnt/work/input -it mgleason/gdal-cli-multiplex`

Or, to test a command that should fail:
`docker run --rm -v $LOCAL_PATH/sample_input_error:/mnt/work/input -it mgleason/gdal-cli-multiplex`

Either way, once the container starts, run:
`python /scripts/task.py`