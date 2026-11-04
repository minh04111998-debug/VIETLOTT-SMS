import os
import sys
import argparse

sys.path.append(r"f:\VIETLOTT-SMS\00_Draft")
import convert_word_to_md

def process_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.startswith('~'): continue
            if file.lower().endswith('.docx') or file.lower().endswith('.doc'):
                filepath = os.path.join(root, file)
                print(f"Processing: {filepath}")
                try:
                    result, error = convert_word_to_md.convert_file(filepath, output_dir)
                    if error:
                        print(f"  Error: {error}")
                    else:
                        print(f"  Success -> {result['output']}")
                        count += 1
                except Exception as e:
                    print(f"  Exception: {e}")
    print(f"Successfully converted {count} files from {input_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    process_directory(args.input, args.output)
