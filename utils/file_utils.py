import uuid
import os

def generate_unique_filename(original_filename):
    # Get the file extension from the original filename
    _, file_extension = os.path.splitext(original_filename)

    # Generate a unique filename using UUID
    unique_filename = str(uuid.uuid4()) + file_extension

    return unique_filename