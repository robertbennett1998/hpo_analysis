from hpo_results import *
import os
from pathlib import Path

results = dict()
result_file_paths = Path.glob(Path("D:\\results\\mnist\\"), "*.results")
for result_file_path in result_file_paths:
    print(result_file_path)
    results[resut_file_path] = Results.load(result_file_path)

print(results)