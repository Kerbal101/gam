import os

# Replace the extension ID with the one you want to delete
extension_id = "extension_id_here"

# Find the user data directory for Chrome
if os.name == "nt":
    # Windows
    app_data = os.getenv("LOCALAPPDATA")
    user_data_dir = os.path.join(app_data, "Google\\Chrome\\User Data\\Default\\Extensions")
else:
    # Mac or Linux
    user_data_dir = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Extensions")

# Delete the extension directory
extension_path = os.path.join(user_data_dir, extension_id)
if os.path.exists(extension_path):
    os.rmdir(extension_path)
    print(f"Extension with ID {extension_id} has been deleted.")
else:
    print(f"No extension with ID {extension_id} found.")
