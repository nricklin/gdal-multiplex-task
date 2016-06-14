import os, subprocess, json, glob2
outdir = '/mnt/work/output/data'
indir = '/mnt/work/input/'

input_data = json.load(open('/mnt/work/input/ports.json'))

cmd = input_data['command']
execution_strategy = input_data.get('execution_strategy', 'runonce')

if execution_strategy == 'runonce':
	command = cmd.replace('$indir',indir)
	command = command.replace('$outdir',outdir)
	print command
	try:
		os.makedirs(outdir)
	except:
		pass
	proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
	status = proc.returncode
	print out


status = { "status": "success", "reason": "Ran stuff." }
with open('/mnt/work/status.json', 'w') as outfile:
	json.dump(status, outfile)