import os
import sys
import importlib

from src.handlers import any_message

dps = []
directory = "src/handlers"
ignore_files = ["__init__.py", "any_message.py"]

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py") and file not in ignore_files:
            module_path = os.path.join(root, file)
            module_name = os.path.splitext(os.path.relpath(module_path, directory))[
                0
            ].replace(os.sep, ".")
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            if hasattr(module, "dp"):
                dps.append(module.dp)

dps.append(any_message.dp)
