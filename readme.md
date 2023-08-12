# Archive Assistant

A python script that archives a directory and manages a directory of archives. Designed to run daily.

I use it for archiving my Obsidian Vault, but this script could be used to archive whatever you want. It is set up to never exceed 1 archive per day, I personally have a cron job that runs once per day.

## This project has been archived

For something similar (and a little more advanced) check out [go-archive-it](https://github.com/korbexmachina/go-archive-it)

## What you need to know

- You need to have a file that specifies the directory to be archived on the first line, and the directory that will be managed by the program.
- The predefined path is `~/.config/archive-assistant/config.txt`
  - You can edit this in the file, and it should be the only thing you need to edit

    ```python
    CONST_PATH = os.path.expanduser("~/.config/archive-assistant/config.txt")
    ```
  
  - I will probably add support for specifying this at runtime at some point
- Default archive format is `.zip`
  - ~~At some point I wil probably add support for specifying this at run time~~
  - There is now support for all of the standard formats providet by `shutil`
    - Specify one of the following in your config file
      - 0 = `.zip`
      - 1 = `.tar` (uncompressed)
      - 2 = `.tar.gz`
      - 3 = `.tar.bz2`
      - 4 = `.tar.xz`

### Example config:

```
~/notes
~/vault-archive
2
```

This example tells the program to archive the `~/notes` directory in the `~/vault-archive` directory using the `.tar.gz` format.

## Roadmap

- Migrate to a formatted config file, probably either yaml or toml
- Specify the name of the config at runtime (to allow for use with multiple directories) __or__ allow an arbitrary number of directories to be added to a single config as a list
  - If I end up implementing the second option, I may have the program handle separation of archives by creating and managing subdirectories with the name of the directory that is being archived
