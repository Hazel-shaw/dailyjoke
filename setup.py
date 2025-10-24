from setuptools import setup, find_packages

setup(
    name="dailyjoke",  # 包的名称
    version="0.1.0",   # 包的版本
    packages=find_packages(),  # 自动发现项目中的包
    install_requires=[],  # 包的依赖，若有依赖可从 requirements.txt 读取，比如 `install_requires=open('requirements.txt').read().splitlines()`
    entry_points={
        "console_scripts": [
            "dailyjoke = dailyjoke.Main:run",  # 如果有可执行脚本，这里配置，格式为“命令 = 模块:函数”
        ]
    },
    author="zzh",
    author_email="zihan.zhang@zhichun.org",
    description="test",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Hazel-shaw/dailyjoke",  # 项目的 GitHub 地址
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

install_requires=[
    "requests>=2.28.0",
    "numpy>=1.21.0"
]