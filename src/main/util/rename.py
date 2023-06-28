import os
import loguru
# Function to rename multiple files of a given folder
def main():
    path=r'C:\Users\Admin\Downloads\Modern Family Season 10\\'
    
    for filename in os.listdir(path):
        my_dest = filename[0:20]
        my_dest_clean = my_dest.replace('.', ' ')  + '.mkv'
        my_source =path + filename
        my_dest =path + my_dest_clean
        # rename() function will
        # # rename all the files
        os.rename(my_source, my_dest)
        # Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()