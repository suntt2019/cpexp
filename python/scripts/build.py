import os

antlr = 'java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

print('Start rebuilding compiler front end...')

print('Clean existing files:')
os.chdir('../src/frontend')
print(f'    Enter directory "{os.path.abspath(os.path.curdir)}"')
for f in os.listdir('.'):
    if f.split('.')[-1] == 'g4':
        continue
    if f == '__init__.py':
        continue
    print(f'    Remove file {f}')

print('Run ANTLR:')
print(f'    ANTLR alias is: {antlr}')
cmd = f'{antlr} -Dlanguage=Python3 Hello.g4'
print(f'    Run command: {cmd}')
os.system(cmd)

print('Build finished.')
