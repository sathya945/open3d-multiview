import open3d as o3d
import sys,os
from view_pointcloud import *



def pick_points(list_pcd_files):
    for i in range(0,len(list_pcd_files)):
        n = os.fork()
        if n>0:
            pass
        else:
            view_pointcloud(list_pcd_files[i])
            sys.exit(0)



if __name__ == "__main__":
    list_pcd_files = sys.argv[1:]
    if len(list_pcd_files) == 0:
        print("usage: python view_pointcloud.py  file  file ..")
        print("input atleast one file")
        exit()
    pick_points(list_pcd_files)