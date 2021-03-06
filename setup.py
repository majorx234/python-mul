from distutils.core import setup
setup(
  name = 'mul',         
  packages = ['mul'],   
  version = '1.0',      
  license='MIT',        
  description = 'This package returns multiplication of two integers.',   
  url = 'https://github.com/majorx234/python-mul',   
  download_url = 'https://github.com/majorx234/python-mul.git',  
  scripts=['scripts/mul'], 
  keywords = ['multiplication', 'calculation'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
