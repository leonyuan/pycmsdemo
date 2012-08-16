import os
from datetime import datetime
import web
from admin.util import admin_render


try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

THUMBNAIL_SIZE = (75, 75)


def get_available_name(name):
    """
    Returns a filename that's free on the target storage system, and
    available for new content to be written to.
    """
    dir_name, file_name = os.path.split(name)
    file_root, file_ext = os.path.splitext(file_name)
    # If the filename already exists, keep adding an underscore (before the
    # file extension, if one exists) to the filename until the generated
    # filename doesn't exist.
    while os.path.exists(name):
        file_root += '_'
        # file_ext includes the dot.
        name = os.path.join(dir_name, file_root + file_ext)
    return name


def get_thumb_filename(file_name):
    """
    Generate thumb filename by adding _thumb to end of
    filename before . (if present)
    """
    return '%s_thumb%s' % os.path.splitext(file_name)


def create_thumbnail(filename):
    image = Image.open(filename)

    # Convert to RGB if necessary
    # Thanks to Limodou on DjangoSnippets.org
    # http://www.djangosnippets.org/snippets/20/
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    # scale and crop to thumbnail
    imagefit = ImageOps.fit(image, THUMBNAIL_SIZE, Image.ANTIALIAS)
    imagefit.save(get_thumb_filename(filename))


def get_media_url(path):
    """
    Determine system file's media URL.
    """
    upload_prefix = web.config.upload_media_url_prefix
    if upload_prefix:
        url = upload_prefix + path.replace(web.config.upload_dir, '')
    else:
        url = web.config.static_url + path.replace(web.config.upload_dir, '')

    # Remove any double slashes.
    #return url.replace('//', '/')
    return url #.replace('//', '/')


def get_upload_filename(upload_name):

    # Generate date based path to put uploaded file.
    date_path = datetime.now().strftime('%Y/%m/%d')

    # Complete upload path (upload_path + date_path).
    upload_path = os.path.join(web.config.upload_dir, date_path)

    # Make sure upload_path exists.
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)

    # Get available name and return.
    return get_available_name(os.path.join(upload_path, upload_name))


def get_image_browse_urls(user=None):
    """
    Recursively walks all dirs under upload dir and generates a list of
    thumbnail and full image URL's for each file found.
    """
    images = []

    # If a user is provided and CKEDITOR_RESTRICT_BY_USER is True,
    # limit images to user specific path, but not for superusers.

    browse_path = web.config.upload_dir

    for root, dirs, files in os.walk(browse_path):
        for filename in [os.path.join(root, x) for x in files]:
            # bypass for thumbs
            if '_thumb' in filename:
                continue

            images.append({
                'thumb': get_media_url(get_thumb_filename(filename)),
                'src': get_media_url(filename)
            })

    return images


class upload:
    def POST(self):
        data = web.input(upload={})
        if 'upload' in data:
            filepath = data.upload.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename = filepath.split('/')[-1]
            upload_filename = get_upload_filename(filename)
            fout = open(upload_filename, 'wb+') # creates the file where the uploaded file should be stored
            fout.write(data.upload.file.read())
            fout.close()

        create_thumbnail(upload_filename)

        url = get_media_url(upload_filename)
        return """
        <script type='text/javascript'>
            window.parent.CKEDITOR.tools.callFunction(%s, '%s');
        </script>""" % (data.CKEditorFuncNum, url)


class browse:
    def GET(self):
        req = web.ctx.req
        req.update({
            'images': get_image_browse_urls(),
            })
        return admin_render.browse(**req)

