from setuptools import find_packages, setup



setup(
    name='efficientvit',
    version='0.1',
    packages=find_packages(),
    install_requires = [
        'timm',
        'transformers',
        'einops',
        'opencv-python',
        'timm==0.6.13',
        'tqdm',
        'torchprofile',

        'matplotlib',
        # 'git+https://github.com/zhijian-liu/torchpack.git@3a5a9f7ac665444e1eb45942ee3f8fc7ffbd84e5',
        'transformers',
        'onnx',
        'onnxsim',
        'onnxruntime',
        # 'git+https://github.com/facebookresearch/segment-anything.git',

    ],


)
