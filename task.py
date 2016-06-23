import os, subprocess, json, glob2
outdir = '/mnt/work/output/'
indir = '/mnt/work/input/'

input_data = json.load(open('/mnt/work/input/ports.json'))

cmd = input_data['command']

if execution_strategy == 'runonce':
	command = cmd.replace('$indir',indir)
	command = command.replace('$outdir',outdir)
	print command
	proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
	status = proc.returncode
	print out