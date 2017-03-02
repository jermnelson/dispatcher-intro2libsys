import argparse
import hashlib
import os
import sys



def create(instance_dir="."):
    """Function creates a random SECRET_KEY in the instance/config.py"""
    full_path = os.path.abspath(os.path.join(instance_dir, "config.py"))
    if os.path.exists(full_path):
        return
    else:
        key = hashlib.sha256(os.urandom(76))
        with open(full_path, "w+") as fo:
            fo.write("""SECRET_KEY="{0}" """.format(key.hexdigest()))

parser = argparse.ArgumentParser()
parser.add_argument("directory", 
    default=os.path.abspath("."))
args = parser.parse_args()
create(args.directory)       
