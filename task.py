import subprocess
import json

outdir = '/mnt/work/output/'
indir = '/mnt/work/input/'
out_status = '/mnt/work/status.json'

input_data = json.load(open('/mnt/work/input/ports.json'))

command = input_data['command']

command = command.replace('$indir', indir)
command = command.replace('$outdir', outdir)

print("Running command: ")
print(command)
print('\n')

proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
returncode = proc.returncode

print('STDOUT:')
print(out.decode())
print('\n')

with open(out_status, 'w') as f:
    # Note: return code isn't enough to capture errors that happen in a compound command
    # so use the presence of any error message as an indicator of failure
    if returncode == 0 and err.decode() == '':
        msg = "SUCCESS: Execution of input command completed successfully."
        f.write(json.dumps({'status': 'success',
                            'reason': msg}))
    else:
        msg = "ERROR: Execution of input command failed."
        msg += err.decode()
        f.write(json.dumps({'status': 'failed',
                            'reason': msg}))
        raise subprocess.SubprocessError(msg)


