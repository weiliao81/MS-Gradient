import sys
import math
import os, time
from multiprocessing import Pool

def process_images(name, task_cmd):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    print('[RUN CMD]: %s' % (task_cmd))
    os.system(task_cmd)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    
def get_task_infos():
    cmd_list = []
    # processing subjects dir
    subID_file = '/MorphometricSimilarity/T1_sublist.txt'
    # Splicing terminal command
    cmd_pre = 'export SUBJECTS_DIR=/MorphometricSimilarity/Recon_Result \n mri_surf2surf --hemi rh --srcsubject fsaverage'
    cmd_mid = ' --sval-annot /MorphometricSimilarity/Recon_Result/fsaverage/label/rh.DK1533.aparc.annot --trgsubject '
    cmd_suff = ' --tval /MorphometricSimilarity/Recon_Result/'
    subID = open(subID_file, "r")
    
    for sub in  subID.readlines():
        sub = sub.replace("\n", "")
        
        cmd = cmd_pre +  cmd_mid + sub + cmd_suff + sub + '/label/rh.DK1533.aparc.annot'
        cmd_list.append(cmd)
    return cmd_list, len(cmd_list)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    process_num = 10 
    task_list, task_size = get_task_infos()

    p = Pool(process_num)
    for i in range(task_size):
        p.apply_async(process_images, args=(i,task_list[i],))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
