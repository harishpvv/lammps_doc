from setuptools import setup, find_packages
  
long_description = 'Get documentation of lammps in JupyterNotebook'
  
setup(
        name ='lammps_doc',
        version ='0.0.1',
        author ='Harish PVV',
        author_email ='harishpvv@gmail.com',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='lammps documentation',
        install_requires = ['beautifulsoup4'],
        )
