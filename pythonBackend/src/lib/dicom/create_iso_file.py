import os
from subprocess import run, PIPE


def create_iso_with_original_names(output_iso_path: str, source_dir: str):
    """
    Creates an ISO image using `mkisofs` (or `genisoimage`) while preserving
    original filenames and directory structure.

    Args:
        output_iso_path: The path to the output ISO file.
        source_dir: The path to the source directory.
    """
    try:
        # Check if mkisofs or genisoimage is available
        if run(["mkisofs", "-version"], stdout=PIPE, stderr=PIPE).returncode == 0:
            command = ["mkisofs", "-r", "-J", "-o", output_iso_path, source_dir]
        elif run(["genisoimage", "-version"], stdout=PIPE, stderr=PIPE).returncode == 0:
            command = ["genisoimage", "-r", "-J", "-o", output_iso_path, source_dir]
        else:
            raise Exception("Neither mkisofs nor genisoimage is available.")

        # Run the command
        result = run(command, stdout=PIPE, stderr=PIPE, text=True)

        if result.returncode != 0:
            raise Exception(f"Error creating ISO: {result.stderr}")

        print(f"ISO created successfully: {output_iso_path}")

    except Exception as e:
        print(f"Error: {e}")


# Example Usage
# create_iso_with_original_names("my_iso.iso", "/path/to/your/source/directory")
