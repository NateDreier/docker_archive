"""
The puropose of this program is to quickly pull down any number of containers and put them (tar) in a directory so that they can be moved.
1. Reads in file
2. Pulls down the containers
3. Re-tags the containers
4. Tars (docker save) up the containers in specified directory
5. deletes all the containers that it just pulled down.

Example use case, working in an airgapped network where everything needs to be moved across (CD, HDD/SSD, one-way data diod, etc), means that you are pulling down and 
saving copious amounts of data. Either doing this for one offs or pulling over a bunch of the latest containers. This allows for quick pull, retag, and save.
"""

"""
file example:
foo:1.2.3
bar:3.2.1
baz:7.7.7
"""
