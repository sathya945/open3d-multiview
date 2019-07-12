import open3d as o3d
import sys

def view_pointcloud(list_pcd_files):
    no_of_window = len(list_pcd_files)
    visualizers = [ None ] * no_of_window
    for i in range(0,no_of_window):
        visualizers[i] = o3d.visualization.Visualizer()
        pcd = o3d.io.read_point_cloud(list_pcd_files[i])
        visualizers[i].create_window(window_name=list_pcd_files[i])
        visualizers[i].add_geometry(pcd)
    while True:
        for vis in visualizers:
            vis.update_geometry()
            vis.poll_events()
            vis.update_renderer()

if __name__ == "__main__":
    list_pcd_files = sys.argv[1:]
    if len(list_pcd_files) == 0:
        print("usage: python view_pointcloud.py  file  file ..")
        print("input atleast one file")
        exit()
    view_pointcloud(list_pcd_files)