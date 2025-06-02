from setuptools import setup, find_packages

setup(
    name="GemmaMini",
    version="0.0.1",
    description="""
    About
    -----
    GemmaMini: A minimal and educational PyTorch implementation of Google's Gemma architecture.
    This project includes key components such as Multi-Head Attention, Rotary Positional Embeddings (RoPE),
    RMSNorm, SwiGLU feedforward layers, and a decoder-only Transformer structure inspired by the official Gemma model.
    """,
    author="Atikul Islam Sajib",
    author_email="atikulislamsajib137@gmail.com",
    url="https://github.com/atikul-islam-sajib/GemmaMini",
    packages=find_packages(),
    install_requires=[
        "dvc",
        "dagshub",
        "graphviz",
        "matplotlib",
        "numpy",
        "mlflow",
        "PyYAML",
        "torch",
        "torchview",
        "torchaudio",
        "torchvision",
        "torchsummary",
        "torchmetrics",
        "scikit-image",
        "opencv-python",
        "nltk",
        "python-dotenv",
        "ipykernel",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    keywords="Gemma, transformer, deep-learning, language-model, PyTorch, LLM",
    project_urls={
        "Bug Tracker": "https://github.com/atikul-islam-sajib/GemmaMini/issues",
        "Documentation": "https://github.com/atikul-islam-sajib/GemmaMini",
        "Source Code": "https://github.com/atikul-islam-sajib/GemmaMini",
    },
)
