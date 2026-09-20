from pathlib import Path
import os
from config import CHARACTER_LIMIT



def get_file_content(working_directory, file_path):
    try:
        wd = (Path.cwd() / Path(working_directory)).resolve()
        p = Path(file_path)
        candidate = p.resolve() if p.is_absolute() else (wd / p).resolve()

        # Ensure candidate is inside working directory
        if os.path.commonpath([str(wd), str(candidate)]) != str(wd):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not candidate.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with candidate.open("r", encoding="utf-8", errors="replace") as f:
            content = f.read(CHARACTER_LIMIT)
            # check if there's more data
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'
        return content
    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lists the file content, given a working directory and the filepath",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "THe file path of which to get the content"
                }
            },
            "required": ["file_path"]
        },
    },
}
