# Writing to a file
with open("exap.txt", "w") as f:  # Create or overwrite the file
    f.write("Hello, Python using Project IDX 1, 2, 4\n")    # Write a line to the file
    f.write("Example of file handling in Python.\n")
    f.write("Neon in pink with black.")

 # Reading from the same file
with open("exap.txt", "r") as f:  # Open the file for reading
    content = f.read()             # Read the entire content of the file



print(content)                     # Print the content read from the file