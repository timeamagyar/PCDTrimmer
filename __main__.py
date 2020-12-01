from trimmer import launchTrimmer
import argparse


if __name__ == '__main__':

    if 1:
        # read result bag
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "-pcd_path",
            type=str, help="path to hitachi annotated pcd file to analyze"
        )

        parser.add_argument(
            "-gt_path",
            type=str, help="path to trimmed gt data"
        )

        parser.add_argument(
            "-remove_number_prefix",
            type=bool,
            default=False,
            help="remove number_ prefix"
        )
        args = parser.parse_args()
        pcd_path = args.pcd_path
        gt_path = args.gt_path
        remove_number_prefix = args.remove_number_prefix

        launchTrimmer(pcd_path, gt_path, remove_number_prefix)






