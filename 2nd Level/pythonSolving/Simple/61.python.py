# Get memory in Bytes
# Convert to GB

bytes_input = int(input("Enter a bytes: "))

gigaBytes = bytes_input / (1024 ** 3)

print(f"{bytes_input} bytes = {gigaBytes:.2f} GB ")