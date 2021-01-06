import uuid
import os


def get_path(instance, filename, folder):
    """ Function to make 'upload_to' value of ImageField's """

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(folder, filename)