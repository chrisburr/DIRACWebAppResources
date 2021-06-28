from setuptools import setup
from dirac_webapp_packaging import find_data_files


setup(
    data_files=find_data_files(
        source_dir="src/DIRACWebAppResources/WebApp/static/extjs",
        dest_dir="share/dirac/DIRACWebAppResources/static/extjs",
    )
)
