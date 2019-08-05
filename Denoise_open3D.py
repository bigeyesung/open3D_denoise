# examples/Python/Advanced/outlier_removal.py

import open3d as o3d
import time
if __name__ == "__main__":
    k=12
    m=0.01
    opt = "_k"+ str(k)+ "_m" + str(m)
    prefix = "pcd/"+ opt + "/" + "open3D/"

    filename = "./pcd/Byg72.pcd"
    start_time = time.time()
    print("open3d " + filename + " :")
    pcd = o3d.io.read_point_cloud(filename)
    filename = filename[6:-4]
    cl, ind = o3d.statistical_outlier_removal(pcd, nb_neighbors=k, std_ratio=m)
    pcd = o3d.select_down_sample(pcd, ind)
    o3d.io.write_point_cloud( prefix + filename + opt + ".pcd", pcd)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/Plan3D_1st.pcd"
    start_time = time.time()
    print("open3d " + filename + " :")
    pcd = o3d.io.read_point_cloud(filename)
    filename = filename[6:-4]
    cl, ind = o3d.statistical_outlier_removal(pcd, nb_neighbors=k, std_ratio=m)
    pcd = o3d.select_down_sample(pcd, ind)
    o3d.io.write_point_cloud( prefix + filename + opt + ".pcd", pcd)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")
    
    filename = "./pcd/Plan3D_2nd.pcd"
    start_time = time.time()
    print("open3d " + filename + " :")
    pcd = o3d.io.read_point_cloud(filename)
    filename = filename[6:-4]
    cl, ind = o3d.statistical_outlier_removal(pcd, nb_neighbors=k, std_ratio=m)
    pcd = o3d.select_down_sample(pcd, ind)
    o3d.io.write_point_cloud( prefix + filename + opt + ".pcd", pcd)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/Plan3D_3rd.pcd"
    start_time = time.time()
    print("open3d " + filename + " :")
    pcd = o3d.io.read_point_cloud(filename)
    filename = filename[6:-4]
    cl, ind = o3d.statistical_outlier_removal(pcd, nb_neighbors=k, std_ratio=m)
    pcd = o3d.select_down_sample(pcd, ind)
    o3d.io.write_point_cloud( prefix + filename + opt + ".pcd", pcd)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/17087.pcd"
    start_time = time.time()
    print("open3d " + filename + " :")
    pcd = o3d.io.read_point_cloud(filename)
    filename = filename[6:-4]
    cl, ind = o3d.statistical_outlier_removal(pcd, nb_neighbors=k, std_ratio=m)
    pcd = o3d.select_down_sample(pcd, ind)
    o3d.io.write_point_cloud( prefix + filename + opt + ".pcd", pcd)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")