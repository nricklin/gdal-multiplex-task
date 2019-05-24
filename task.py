import subprocess
import json

outdir = '/mnt/work/output/'
indir = '/mnt/work/input/'

input_data = json.load(open('/mnt/work/input/ports.json'))

command = input_data['command']

command = command.replace('$indir', indir)
command = command.replace('$outdir', outdir)

print("Running command: ")
print(command)
print('\n')

proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
status = proc.returncode

print(out.decode())
print('\n')

if status == 0:
    print("SUCCESS: Execution of input command completed successfully.")
else:
    print("ERROR: Execution of input command failed.")
    print(err.decode())

