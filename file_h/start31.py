import os

# Specify the file to be deleted
file_to_delete = "exap.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)  # Delete the file
    print(f"File '{file_to_delete}' deleted successfully.")
else:
    print(f"The file '{file_to_delete}' does not exist.")