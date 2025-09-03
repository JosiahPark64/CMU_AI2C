import os
from os.path import join, getsize

def get_path_depth(path):
    path = os.path.normpath(path)
    return len(path.split(os.sep))



# path: A str that identifies a relative or an absolute path to the directory that will be inspected and for which a report needs to be generated.

# report_file_path: A str that identifies the path to the file where the report will be written.

# show_files: A bool that indicates if files should be listed in the report. If set to True the report lists the directories as well as the files; when set to False the report omits the lines listing the files and only lists directories. The parameter has True set as the default value.

# num_files: A bool that indicates if the number of files should be reported for directories. If set to True the names of the directories are followed by a space and a parenthetical containing the number of files that are directly contained within that directory (not its sub-directories) and a keyword files. If set to False the parenthetical is omitted. The parameter is set to False value as its default value.
# Example: operations (4 files)

# file_size: A bool that indicates if the file size should be reported for files. If set to True the names of the files are followed by a space and a parenthetical containing the size of the respective file in bytes and a keyword bytes. If set to False the parenthetical is omitted.
# Example: prepare.py (24850 bytes)

# hl: A str or None that specifies the extension of files to be highlighted with a right-to-left arrow. If set to a str value, the files with the extension that matches that str argument should be highlighted by <-- at the end.
def generate_dir_report(path: str, report_file_path: str, show_files: bool, num_files: bool, file_size: bool):
    file_count = 0
    directory_prefix = '|-+'
    file_prefix = '|--'
    main_path_depth = get_path_depth(path)

    with open(report_file_path,'w') as report:
        for root, dirs, files in sorted(os.walk(path)):
            #root var is a path to the current directory. every single directory will be treated as root in exactly one iteration
            #dirs variable has a list with names of the directories that are contained directly in the root directory
            #files variable has a list with names of the files that are contained directly in the root dir
            
            #track files per directory
            if num_files == True:
                for file_x in sorted(files):
                    file_count+=1
            
            # store variable `dir_indent` which you can compute as <depth of the root> - `main_path_depth` - 1
            dir_indent = get_path_depth(root) - main_path_depth - 1

            # store variable `file_indent` which you can compute as `dir_indent` + 1
            file_indent = dir_indent +1

            # write the directory name from the `root` string into the `out` file as a single line; use `dir_indent` 
            # to determine prefix and indentation
            if dir_indent ==-1:
                line = f'+ {os.path.basename(path)} ({file_count} files)\n'
            else:
                line = f'{"  "*dir_indent}{directory_prefix} {os.path.basename(root)} ({file_count} files)\n'
            print(line)          #testing output for the in browser submission
            report.write(line)
            
            # write the `file_name` string into the `out` file as a single line; use `file_indent` to determine prefix and indentation
            if show_files == True:
                for file_name in sorted(files):
                    
                    if file_size == True:           #account for file size
                        file_sz = os.path.getsize(f"{root}/{os.path.basename(file_name)}")
                        file_line = f'{"  "*file_indent}{file_prefix} {os.path.basename(file_name)} ({file_sz} bytes)\n'
                    else:
                        file_line = f'{"  "*file_indent}{file_prefix} {os.path.basename(file_name)}\n'

                    print(file_line)          #testing output for the in browser submission
                    report.write(file_line)
            
            #reset file count
            file_count =0

if __name__ == '__main__':
    generate_dir_report('data/dir-top', 'dir-report.txt',True, True, True)