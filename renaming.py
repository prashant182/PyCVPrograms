import os
import glob

i=0;
#renaming batch files
for filename in glob.glob('*.*'):
    os.rename(filename,'PATH'+str(i)+'.JPEG')
    i=i+1