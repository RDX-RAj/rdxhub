
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'rdxhub',        
  packages = ['rdxhub'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'rdxhub Logo Generator', 
  author = 'RDX RAj',                  
  author_email = 'vdjrdx29@gmail.com',     
  url = 'https://github.com/RDX-RAj/rdxhub',   
  download_url = 'https://github.com/RDX-RAj/rdxhub/archive/1.2.tar.gz',    
  keywords = ['rdxhub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
