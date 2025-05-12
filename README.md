# CV101: Computer Vision Fundamentals

This repo includes hands-on Jupyter notebooks to learn computer vision using OpenCV on macOS (Apple Silicon) and NVIDIA GPUs.

## Notebooks

- `cv101-week1-lowCode.ipynb` – Starter: load and process images
- `cv101-week1-full.ipynb` – Full GPU-optional solution with CUDA hooks
- `cv101-week1-apple-solution.ipynb` – Apple Silicon optimized version

## Setup

```bash
conda env create -f environment.yml
conda activate cv101
jupyter lab
```

## Sample Image

Place any image/video you want to test inside `./images/`. for example `./images/bananas.jpg`.

## Sample script

Run webcam script at `./scripts/cam.py` with

```bash
python scripts/cam.py
```
