# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path


def theWork():
    for root, dirs, files in os.walk("old_files/"):
        p = os.path.abspath(root)
        new_loc = root.replace("old_files", "new_files")
        if not os.path.exists(new_loc):
            os.makedirs(new_loc)
        total_files = str(len(files))
        for num, file in enumerate(files, start=1):
            if file.endswith((".htm", ".html", ".asp", ".aspx")):
                sys.stdout.write("\rConverting file " + str(num) + " of " + total_files)
                sys.stdout.flush()
                fp = "{0}/{1}".format(p, file)
                nfl = fp.replace("old_files", "new_files")
                with open(nfl, 'w+') as nf:
                    with open(fp, "rb") as f:
                        lines = f.readlines()
                        for line in lines:
                            try:
                                line = line.decode("windows-1252")
                                nl = line.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')
                                nl.encode("utf-8")
                                nf.write(nl)
                            except Exception as e:
                                tmp1 = "c".encode("utf-8")
                                tmp2 = "i".encode("utf-8")
                                line = line.replace(b'\x8d', tmp1).replace(b'\x8f', tmp2)
                                line = line.decode("utf-8")
                                nl = line.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')
                                nl.encode("utf-8")
                                nf.write(nl)

if __name__ == "__main__":
    try:
        print("Starting conversion...")
        theWork()
        print("\nConversion done.")
    except Exception as e:
        print(e)
