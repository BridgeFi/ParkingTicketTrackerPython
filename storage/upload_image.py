import datetime
import six

from common import util


def set_filename(filename):
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = filename.rsplit('.', 1)
    return "{0}_{1}.{2}".format(basename, date, extension)


def upload_file(file_stream, filename, content_type):
    bucket = util.get_bucket()
    blob = bucket.blob(filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type
    )
    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url
