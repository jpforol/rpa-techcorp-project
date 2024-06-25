import os

def create_directory(path):
    """ Create a directory if it does not exist """
    if not os.path.exists(path):
        os.makedirs(path)

# Example usage
if __name__ == "__main__":
    create_directory('data/processed')
