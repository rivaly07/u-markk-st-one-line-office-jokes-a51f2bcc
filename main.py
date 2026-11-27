import os
import sys

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry_file:
    entry_file.write("The meeting about cutting down on meetings ran forty minutes over, so we voted to continue it next week.")
