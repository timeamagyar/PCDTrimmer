import pypcd
import pprint
import numpy as np
import re
import os
import glob
from numpy.lib.recfunctions import structured_to_unstructured

CLASS_NAMES = ['BG', 'person']

def keyFunc(afilename):
    nondigits = re.compile("\D")
    return int(nondigits.sub("", afilename))


def launchTrimmer(pcd_path, gt_path, remove_number_prefix):
    gt_list = []
    for file in sorted(glob.glob(os.path.join(pcd_path, '*.pcd')), key=keyFunc):
        print(file)
        pcd_file = os.path.basename(file)
        base = os.path.splitext(pcd_file)[0]
        if remove_number_prefix:
            base = base.rsplit("_",1)[1]

        gt_list.append(base)

        gt_file = os.path.join(gt_path, base + "." + 'txt')
        print(os.path.join(gt_path, base + "." + 'txt'))
        # load cloud.pcd
        cloud = pypcd.PointCloud.from_path(file)
        pprint.pprint(cloud.get_metadata())

        # convert the structured numpy array to a ndarray
        trimmed_cloud = structured_to_unstructured(cloud.pc_data)

        # print the shape of the new array
        print(trimmed_cloud.shape)

        # That looks good! Now we can delete the xyz columns and only keep the class + label predictions
        trimmed_cloud_data = np.delete(trimmed_cloud, [0, 1, 2], axis=1)
        trimmed_cloud_data = trimmed_cloud_data.astype(np.int32)
        trimmed_cloud_data[:, 1] = trimmed_cloud_data[:,1] + 1

        class_ids = trimmed_cloud_data[:,0]
        instance_ids = trimmed_cloud_data[:,1]
        class_names = np.array([CLASS_NAMES[i] for i in class_ids])
        gt = np.vstack((instance_ids, class_names)).T
        np.savetxt(gt_file, gt, fmt="%s")
        print("succeeded")
    print(gt_list)
