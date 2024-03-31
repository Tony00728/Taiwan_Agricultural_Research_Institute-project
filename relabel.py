import os

def convert_labels_to_zero(source_folder, destination_folder):
    # 確保目標資料夾存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 遍歷源資料夾中的所有文件
    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):  # 檢查是否為YOLO格式的label文件
            source_file_path = os.path.join(source_folder, filename)
            destination_file_path = os.path.join(destination_folder, filename)

            # 讀取原始標籤文件
            with open(source_file_path, 'r') as file:
                lines = file.readlines()

            # 更改所有標籤為0
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if parts:  # 確保行中有內容
                    parts[0] = '4'  # 將類別編號更改為0
                    new_lines.append(' '.join(parts) + '\n')

            # 寫入新的標籤文件到目標資料夾
            with open(destination_file_path, 'w') as file:
                file.writelines(new_lines)


# 使用範例
source_folder = r'/home/tony/Downloads/NEW/tree04'
destination_folder = r'/home/tony/Downloads/NEW/04'
convert_labels_to_zero(source_folder, destination_folder)
