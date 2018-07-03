import os

# Each website you crawl is a separate project (folder)

def create_project_dir(directory):
    if not os.path.exists(directory):               # Create directory only if it does not exist
        print('Creating project ' + directory)
        os.makedirs(directory)                      # Create directory

# Create queue and crawled files (if not created)

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'     # In this project, we will have a file named queue.txt containing list of pages to be crawled
    crawled = project_name + '/crawled.txt'    # contains list of pages which have been crawled
    if not os.path.isfile(queue):               # If queue file doesn't exist, create it and write base_url to it
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file

def append_to_file(path, data):
    with open(path, 'a') as file:                   # file is a reference to the opened file in append mode
        file.write(data + '\n')


# Delete all the contents of a file

def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to a set item

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:                      # 'rt' means read text file
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a new line in the file

def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
