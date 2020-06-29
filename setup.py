from setuptools import setup, find_packages

setup(
    name="demobuildissue",
    version="0.0",
    description="demobuildissue",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web wsgi",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    demo_say_hello = demobuildissue.scripts.sayhello:main
    """,
)
