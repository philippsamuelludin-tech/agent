import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_path, file_path))
        valid_target_dir = os.path.commonpath([working_path, target_path]) == working_path

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args != None:
            command.extend(args) 

        process = subprocess.run(
            command,
            cwd=working_path,
            capture_output=True,
            text=True,
            timeout=30,
            )

        output_string = ""
        if process.returncode != 0:
            output_string += f"Process exited with code {process.returncode}\n"

        if process.stdout != "":
            output_string += f"STDOUT: {process.stdout}\n"
        if process.stderr != "":
            output_string += f"STDERR: {process.stderr}\n"
        if process.stdout == "" and process.stderr == "":
            output_string += "no output"

        return output_string
        
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "An arry of args to parse in to the python file"
                }
            },  
            "required": ["file_path"]
        },
    },
}
