import open3d as o3d
import sys
from multiprocessing import Process
from pointscript import *



def pick_points(list_pcd_files):
    proc = []
    for i in range(0,len(list_pcd_files)):
        p = Process(target = view_pointcloud,args =(list_pcd_files[i],))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()




if __name__ == "__main__":
    list_pcd_files = sys.argv[1:]
    if len(list_pcd_files) == 0:
        print("usage: python view_pointcloud.py  file  file ..")
        print("input atleast one file")
        exit()
    pick_points(list_pcd_files)