import subprocess
import uuid
import os

def run_demucs(input_file_path: str):
    file_id = str(uuid.uuid4())
    output_dir = f"separated/{file_id}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    subprocess.run(
        ["demucs", "-o", output_dir, "-n", "mdx_extra", input_file_path],
        check=True
    )

    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    model_output = os.path.join(output_dir, "mdx_extra", base_name)

    vocals = os.path.join(model_output, "vocals.wav")
    instrumental = os.path.join(model_output, "no_vocals.wav")

    return vocals, instrumental, file_id
