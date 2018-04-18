import pdb
import subprocess
from subprocess import check_output
from sys import argv
import glob

inFiles = glob.glob('input_spec/*.txt')
library = 'libnor36'
outputFile = 'output.txt'
logFile = 'log.txt'
roughType = 2
nIter = 3

dirOutput = []

for oneFile in inFiles:
    cmd = " ".join(['mkclass',oneFile,library,outputFile,logFile,
                    str(roughType),str(nIter)])
    dirOutput.append('Command to be executed:')
    dirOutput.append(cmd)
    try:
        out = check_output(cmd,shell=True)
        dirOutput.append(out)
    except subprocess.CalledProcessError as e:
        saveout="command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output)
        dirOutput.append(saveout)
    except:
        saveout="Unknown error for command:"+cmd
        dirOutput.append(saveout)
        
with open('mkclass_output.txt','w') as outputfile:
    for line in dirOutput:
        outputfile.write(line+'\n')
