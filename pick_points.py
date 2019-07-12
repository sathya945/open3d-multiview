import open3d as o3d
import sys
import os
import time



def write_to_file(file_name,array):
    dire = "pickedpoints"
    if not os.path.exists(dire):
        os.makedirs(dire)
    MyFile=open(dire+"/"+file_name,'w')
    for element in array:
        MyFile.write(str(element))
        MyFile.write('\n')
    MyFile.close()


def pick_points(list_pcd_files):
    no_of_window = len(list_pcd_files)
    visualizers = [ None ] * no_of_window
    for i in range(0,no_of_window):
        visualizers[i] = o3d.visualization.VisualizerWithEditing()
        pcd = o3d.io.read_point_cloud(list_pcd_files[i])
        visualizers[i].create_window(window_name=os.path.basename( list_pcd_files[i]))
        visualizers[i].add_geometry(pcd)
        visualizers[i].run()
        visualizers[i].destroy_window()
        a = visualizers[i].get_picked_points()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        write_to_file(os.path.basename( list_pcd_files[i])+timestr+".txt",a)

if __name__ == "__main__":
    list_pcd_files = sys.argv[1:]
    if len(list_pcd_files) == 0:
        print("usage: python view_pointcloud.py  file  file ..")
        print("input atleast one file")
        exit()
    pick_points(list_pcd_files)