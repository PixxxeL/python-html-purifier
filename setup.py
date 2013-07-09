from distutils.core import setup
#import markdown2
import purifier

#with open('README.md') as fh:
#    long_description = fh.read()
#markdowner = markdown2.Markdown()

setup(
    name = "html-purifier",
    version = purifier.__version__,
    packages = ["purifier"],
    url = 'https://github.com/PixxxeL/python-html-purifier',
    author = 'pixel',
    author_email = 'ivan.n.sergeev@gmail.com',
    maintainer = 'pixel',
    maintainer_email = 'ivan.n.sergeev@gmail.com',
    license = 'GPL3',
    description = 'Cuts the tags and attributes from HTML that are not in the whitelist. Their content is leaves.',
    #long_description = markdowner.convert(long_description),
    download_url = 'https://github.com/PixxxeL/python-html-purifier/archive/master.zip',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
