
import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_path, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_path, target_dir]) == working_path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        items = []
        for item in os.listdir(target_dir):
            item_path = "/".join([target_dir, item])
            is_dir = True if os.path.isdir(item_path) else False
            size = os.path.getsize(item_path)
            items.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        return f"Result for '{directory}' directory:\n{"\n".join(items)}"
    except Exception as e:
        return f"Error: {e}"