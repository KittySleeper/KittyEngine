import os

def rename_json_files(base_path):
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)

        if os.path.isdir(folder_path):  # Ensure it's a directory
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                if file_name.endswith(".json") and not file_name.endswith("-hard.json") and not file_name.endswith("-easy.json"):
                    new_file_name = os.path.splitext(file_name)[0] + "-normal.json"
                    new_file_path = os.path.join(folder_path, new_file_name)

                    if not os.path.exists(new_file_path):  # Avoid conflicts
                        os.rename(file_path, new_file_path)
                        print(f'Renamed: "{file_name}" -> "{new_file_name}" in "{folder_name}"')
                    else:
                        print(f'Skipped: "{file_name}" in "{folder_name}" (Target name already exists)')

if __name__ == "__main__":
    path = input("Enter the base directory path: ")

    if os.path.exists(path) and os.path.isdir(path):
        rename_json_files(path)
    else:
        print("Invalid path. Please enter a valid directory.")