import os
from tqdm import tqdm
import shutil

src_dir = os.path.join(f"inria/Train/pos")
src_ann_dir = os.path.join(f"inria/Train/annotations")
src_yolo_labels_dir = os.path.join(f"inria/Train/pos/yolo-labels")

tgt_dir = os.path.join(f"inria_100/Train/pos")
tgt_ann_dir = os.path.join(f"inria_100/Train/annotations")
tgt_yolo_labels_dir = os.path.join(f"inria_100/Train/pos/yolo-labels")
os.makedirs(tgt_dir, exist_ok=True)
os.makedirs(tgt_ann_dir, exist_ok=True)
os.makedirs(tgt_yolo_labels_dir, exist_ok=True)

src_ims = [im for im in os.listdir(src_dir) if im.endswith(".png")]
sel_ims = src_ims[:100]

pos_lines = []
ann_lines = []
for im in tqdm(sel_ims):
    ann = im.split('.')[0]+'.txt'

    shutil.copy2(os.path.join(src_dir, im), tgt_dir)
    shutil.copy2(os.path.join(src_ann_dir, ann), tgt_ann_dir)
    shutil.copy2(os.path.join(src_yolo_labels_dir, ann), tgt_yolo_labels_dir)

    pos_lines.append(f"Train/pos/{im}")
    ann_lines.append(f"Train/annotations/{ann}")

with open(os.path.join(f"inria_100/Train", "pos.lst"), "w") as f:
    for line in pos_lines:
        f.write(line + "\n")

with open(os.path.join(f"inria_100/Train", "annotations.lst"), "w") as f:
    for line in ann_lines:
        f.write(line + "\n")

