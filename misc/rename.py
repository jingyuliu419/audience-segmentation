import os

def re_fileName():
    # Get the current working directory where the script is located
    current_path = os.path.dirname(os.path.abspath(__file__))
    last_folder_name = os.path.basename(current_path)
    
    file_list = os.listdir(current_path)
    num = 0  # Start numbering from 0, as per your requirement
    
    for file in file_list:
        # Only rename files, skip directories
        if os.path.isfile(os.path.join(current_path, file)):
            _, extension = os.path.splitext(file)
            new_file = f"{last_folder_name}_{num}{extension}"
            old_file_path = os.path.join(current_path, file)
            new_file_path = os.path.join(current_path, new_file)
            
            os.rename(old_file_path, new_file_path)
            print(f"文件 {old_file_path} 重命名成功，新的文件名为：{new_file_path}")
            num += 1

if __name__ == '__main__':
    re_fileName()
