import os, zlib, argparse

PACK_FILE_PATH = "robot_packed"
OUTPUT_FOLDER = "data/fighter/robot/script/"
OUTPUT_FILE = "packed"
OUTPUT_PATH = OUTPUT_FOLDER + OUTPUT_FILE
PACK_OFFSET = 0xB380
COMPRESSED_SIZE = 0x1B1D0
UNCOMPRESSED_SIZE = 0x5B2E0

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

parser = argparse.ArgumentParser(description="pack ROB's mscsb files")
parser.add_argument('in_file')
in_file = parser.parse_args().in_file

with open(in_file, 'rb') as f:
    data = f.read()

assert len(data) <= UNCOMPRESSED_SIZE

data += b'\0' * (UNCOMPRESSED_SIZE - len(data))

compressed_data = zlib.compress(data)

assert len(compressed_data) <= COMPRESSED_SIZE

compressed_data += b'\0' * (COMPRESSED_SIZE - len(compressed_data))

with open(PACK_FILE_PATH, 'rb') as f:
    pack_file_data = f.read()

with open(OUTPUT_PATH, 'wb') as f:
    f.write(pack_file_data[:PACK_OFFSET])
    f.write(compressed_data)
    f.write(pack_file_data[PACK_OFFSET + COMPRESSED_SIZE:])
