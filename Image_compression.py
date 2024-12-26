from PIL import Image
import argparse
# 打开图像文件



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_picture', type=str, default=None)
    parser.add_argument('--out_picture', type=str, default=None)
    args = parser.parse_args()
    img = Image.open(args.in_picture)

    # 定义新的分辨率，例如降低到原来的一半
    new_width = img.width // 2
    new_height = img.height // 2


    # 最近邻插值
    img_resized_nearest = img.resize((new_width, new_height), Image.NEAREST)

    # 保存降低分辨率后的图像
    img_resized_nearest.save(args.out_picture)


