import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_path, file_path))
        valid_target_dir = os.path.commonpath([working_path, target_path]) == working_path

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "w", encoding="UTF-8") as file:
            chars_written = file.write(content)

        return f'Successfully wrote to "{file_path}" ({chars_written} characters written)'


    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file where the content should be written",
                },
                "content": {
                    "type": "string",
                    "description": "The content to be written",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
    