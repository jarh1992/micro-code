from pathlib import Path
import cv2
import yaml
from numpy import array
from numpy import rint
from numpy import zeros_like


def extract_segmentation(
    img_path: str, rimg_path: str, lbl_path: str, dest: str, dsfile: str
) -> None:
    """
    function to extract segmented images according to the info in the label file

    Parameters
    ----------
    img_path: image path
    rimg_path: reference image path
    lbl_path: path of the txt file with label info
    dest: destination folder path
    dsfile: dataset.yaml file path
    """
    image_path = Path(rf"{img_path}")
    label_path = Path(rf"{lbl_path}")
    dest_path = Path(rf"{dest}")
    img_name = image_path.stem
    image = cv2.imread(str(image_path))
    ref_image_path = Path(rf"{rimg_path}") if rimg_path != "" else None
    ref_image = cv2.imread(str(ref_image_path)) if ref_image_path else None
    h, w = image.shape[:2]
    with open(dsfile, "r") as file:
        data = yaml.safe_load(file)
    with open(label_path) as label:
        for i, line in enumerate(label.readlines()):
            ln = line.split()
            categ = int(ln[0])
            categ_name = data["names"][categ]
            categ_folder = dest_path / categ_name
            categ_folder.mkdir(parents=True, exist_ok=True)
            seg_coords = array(list(map(float, ln[1:]))).reshape((-1, 1, 2))
            seg_coords[:, :, 0] = seg_coords[:, :, 0] * w
            seg_coords[:, :, 1] = seg_coords[:, :, 1] * h
            seg_coords = rint(seg_coords).astype(int)

            mask = zeros_like(image, dtype=uint8)
            cv2.fillPoly(mask, [seg_coords], color=(255, 255, 255))
            roi = cv2.bitwise_and(image, mask)

            x, y, w1, h1 = cv2.boundingRect(seg_coords)
            polygon_only = roi[y : y + h1, x : x + w1]
            cv2.imwrite(f"{str(categ_folder)}/{img_name}_seg_{i}.png", polygon_only)

            if ref_image:
                ref_roi = cv2.bitwise_and(ref_image, mask)
                ref_polygon_only = ref_roi[y : y + h1, x : x + w1]
                cv2.imwrite(
                    f"{str(categ_folder)}/{img_name}_seg_{i}_ref.png", ref_polygon_only
                )


def main()
	img_path = enter_str_input("Enter the absolute path of the image: ")
	rimg_path = input("Enter the absolute path of the reference image (enter if not): ")
	label_path = enter_str_input("Enter the absolute path of the image label: ")
	dest_path = enter_str_input("Enter the absolute path of the destination folder: ")
	dataset_yaml_path = enter_str_input("Enter the absolute path of the dataset.yaml file: ")
	extract_segmentation(img_path, rimg_path, label_path, dest_path, dataset_yaml_path)


if __name__ == '__main__':
	main()
