import os
 
def add_prefix_suffix(directory, prefix, suffix):
    for filename in os.listdir(directory):
        new_filename = prefix + filename + suffix
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
 
# 示例用法
add_prefix_suffix('./', '', '.in')