import os


def list_directories(s):

    def dir_list(d):
        # Introduce nonlocal variable tab_stop to subfunction
        nonlocal tab_stop
        # Get list of directory
        files = os.listdir(d)
        for f in files:
            # Get path of each item in the list
            current_dir = os.path.join(d, f)
            # Check if it is a directory or file
            if os.path.isdir(current_dir):
                print('\t' * tab_stop + 'Directory ' + f)
                # Extend the tab level for the subdirectory
                tab_stop += 1
                # Explore Subdirectory
                dir_list(current_dir)
                # Retract the tab level after the subdirectory is completed
                tab_stop -= 1
            else:
                # No directory -> Must be file
                print('\t' * tab_stop + f)
    # Tab stops in outer scope keep track of the directory level
    tab_stop = 0
    # Check if filepath exists and pass initial argument s to subfunction
    if os.path.exists(s):
        print('Directory Listing of ' + s)
        dir_list(s)
    else:
        print(s + ' does not exist')


# listing = os.walk('d:/Python')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for f in files:
#         print(f)

list_directories('d:/Python')
