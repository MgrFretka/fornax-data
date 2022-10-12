import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
        name='discord-ext-forms', 
        version='3.10.6',
        packages=["python.learn.mpfd"], 
        author='freteq', 
        author_email='liton.developers@gmail.com', 
        license='MIT',
        description='Stworzono do nauki pyhtona, extensions należą do serwera Litona!.', 
        long_description=long_description, 
        long_description_content_type='text/markdown', 
        url='https://github.com/', 
#        packages=setuptools.find_packages(), 
        classifiers=[
            'Programming Language :: Python :: 3.8', 
            'Programming Language :: Python :: 3.9', 
            'Programming Language :: Python :: 3.10', 
            'License :: OSI Approved :: MIT License', 
            'Operating System :: OS Independent', 
            'Topic :: Communications :: Chat', 
            'Intended Audience :: Developers', 
        ], 
        python_requires='>=3.7', install_requires=['discord.py>=1.5']
)