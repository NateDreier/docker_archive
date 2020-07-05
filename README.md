# Docker Archive

Docker Archive is a simple Python script that takes in a list of `<docker_images>:<tags>`, pulls them all down, re-tags them if needed and tars them up,  
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
https://github.com/NateDreier/docker_archive.git
```

## Usage
### Prep
Have a text file populated with a list of `image:tag`'s. See example below:
```bash
# foo.txt
hello-world:latest
centos:8
ubuntu:20.04
jitsi/jvb:latest
jitsi/jicofo:4627-1
```
### Run 
```bash
# Option one
./docker_archive.py <name_of_.txt>
# Example: 
./docker_archive.py img.txt

# Option two
./docker_archive.py <name_of_.txt> <name_of_repository>
# Example:
./docker_archive.py img.txt harbor.myDomain.io
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
