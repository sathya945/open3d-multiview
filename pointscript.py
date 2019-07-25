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



def view_pointcloud(pcd_file):
    visualizer = o3d.visualization.VisualizerWithEditing()
    pcd = o3d.io.read_point_cloud(pcd_file)
    visualizer.create_window(window_name=os.path.basename( pcd_file))
    visualizer.add_geometry(pcd)
    visualizer.run()
    visualizer.destroy_window()
    a = visualizer.get_picked_points()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    write_to_file(os.path.basename( pcd_file)+timestr+".txt",a)



