# Archive Assistant

A python script that automatically archives a directory and manages a directory of archives. Designed to run daily.

I use it for archiving my Obsidian Vault, but this script could be used to archive whatever you want. It is set up to never exceed 1 archive per day, I personally have it set up with a cron job.

## What you need to know

- You need to have a file that specifies the directory to be archived on the first line, and the directory that will be managed by the program.
- The predefined path is `~/.config/autoArchive/archivePaths.txt`
  - You can edit this in the file, and it should be the only thing you need to edit

    ```python
    CONST_PATH = os.path.expanduser("~/.config/autoArchive/archivePaths.txt")
    ```
  
  - I will probably add support for specifying this at runtime at some point
- default archive format is `.tar.gz`
  - at some point I wil probably add support for specifying this at run time

### Example config:

```
~/notes
~/vault-archive
```
