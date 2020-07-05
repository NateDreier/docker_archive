#!/usr/bin/env python3

import sys
import re
import os
from os import path
import concurrent.futures  # https://docs.python.org/3/library/concurrent.futures.html
import docker  # https://docker-py.readthedocs.io/en/stable/

"""
TODO: Take the below vars out of global
TODO: Use Pathlib
TODO: Use Argparse
TODO: Make the code more reusable by sticking it all in a class.
"""
cli = docker.APIClient(base_url="unix://var/run/docker.sock")
current_dir = os.getcwd()
repository = sys.argv[2] if len(sys.argv) >= 3 else None
tar_dir = os.path.join(current_dir, "move")


if not path.exists(tar_dir):
    os.mkdir(tar_dir)


def simple_image(image: str):
    if len(sys.argv) >= 3:
        img, t = image.split(":")
        image = f"{img}:{t}"
        new_image = f"{repository}/{image}"
        print("hello, sys.argv >= 3")
        print(f"Pulling, retagging, saving and rmi'ing: {image}")
        # Pulls the container
        cli.pull(image)
        # Tags the container with the new tag
        cli.tag(image, f"{repository}/{img}", t)
    else:
        img, t = image.split(":")
        image = f"{img}:{t}"
        new_image = f"{image}"
        print("hello, sys.argv")
        print(f"Pulling, retagging, saving and rmi'ing: {image}")      
        cli.pull(image)
        cli.tag(image, f"{img}", t)

    new_image_name = f"{img}{t}.tar"
    im = cli.get_image(new_image)
    with open(os.path.join(tar_dir, new_image_name), "wb+") as f:
        for chunk in im:
            f.write(chunk)

    # Deletes all downloaded images
    cli.remove_image(image)
    cli.remove_image(new_image)


def complex_image(image: str):
    if len(sys.argv) >= 3:
        i, t = image.split(":")
        img_reg = i.split("/")
        img = img_reg[1].strip()
        image = f"{i}:{t}"
        new_image = f"{repository}/{image}"

        print(f"Pulling, retagging, saving and rmi'ing: {image}")
        # Pulls the container
        cli.pull(image)
        # Tags the container with the new tag
        cli.tag(image, f"{repository}/{i}", t)
     
    else:    
        img_reg = i.split("/")
        img = img_reg[1].strip()
        image = f"{i}:{t}"
        new_image = f"{image}"

        print(f"Pulling, retagging, saving and rmi'ing: {image}")
        # Pulls the container
        cli.pull(image)
        # Tags the container with the new tag
        cli.tag(image, f"{i}", t)
     
    new_image_name = f"{img}{t}.tar"
    im = cli.get_image(new_image)
    with open(os.path.join(tar_dir, new_image_name), "wb+") as f:
        for chunk in im:
            f.write(chunk)

    # Deletes all downloaded images
    cli.remove_image(image)
    cli.remove_image(new_image)


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if "/" not in line:
                executor.submit(simple_image, line)
            else:
                executor.submit(complex_image, line)
