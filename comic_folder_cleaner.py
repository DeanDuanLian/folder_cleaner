import sys, shutil, re
from pathlib import Path

def get_comic_folder(original_folder):
    pattern = re.compile(r'\[\d+\](\[.*\]\[.*\].+)(?:第| \(| ：| \(|\(|（| \d+)')
    result = pattern.findall(str(original_folder))
    if result:
        comic_folder = result[0].strip().strip('：').strip()
    if not result:
        pattern_2 = re.compile(r'\[\d+\](\[.*\]\[.*\].+)(?:\d+|[０-９]+|[Ａ-ｚ]+\[.+)')
        result = pattern_2.findall(str(original_folder))
        if result:
            comic_folder = result[0].strip().strip('：').strip()
        if not result:
            pattern_3 = re.compile(r'\](\[[^\]]+\].+?) \[')
            result = pattern_3.findall(str(original_folder))
            if result:
                comic_folder = result[0].strip().strip('：').strip()
            else:
                comic_folder =  'unsorted'
    return comic_folder

def move_folder(target:Path, folder:Path):
    original_name = folder.name
    comic_folder = get_comic_folder(original_name)
    target_folder = target/comic_folder/original_name
    shutil.move(folder,target_folder)
    print(f'Moved {original_name} to {comic_folder} successfully.')
    return True

def main():
    print('Process begins')
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    input_path_type = Path(input_path)
    output_path_type = Path(output_path)
    print(f'Input path: {input_path_type}\nOutput Path: {output_path_type}')
    input_folders = list(input_path_type.glob('*'))
    # print(input_folders)
    for folder in input_folders:
        # print(f'Input subfolders: {folder}')
        move_folder(target=output_path_type, folder=folder)
    print('All processed')

if __name__=='__main__':
    main()