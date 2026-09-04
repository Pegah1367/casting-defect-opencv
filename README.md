# Casting Defect Detection with OpenCV

![CI](https://github.com/Pegah1367/casting-defect-opencv/actions/workflows/ci.yml/badge.svg)

This project explores classical computer vision techniques for detecting
possible defects in casting products using OpenCV.

## Project Goal

The goal is to learn and apply fundamental image-processing techniques
for casting defect analysis.

## Main Pipeline

Image
→ Grayscale
→ CLAHE
→ Blur
→ Black Hat
→ ROI
→ Otsu Thresholding
→ Morphology
→ Contours
→ Candidate Defect
→ Final Result

## Computer Vision Concepts

This project includes:

- Grayscale conversion
- RGB and HSV
- Color segmentation
- CLAHE
- Histogram and Histogram Equalization
- Average Blur
- Gaussian Blur
- Median Blur
- Black Hat Morphology
- ROI masks
- Otsu Thresholding
- Morphological Opening
- Contours
- Bounding Boxes

## Average Blur

Average Blur was added as a reusable Python function:

`src/average_blur.py`

It is tested using:

`tests/test_average_blur.py`

## Continuous Integration

This project uses GitHub Actions for CI.

The workflow automatically:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Runs automated tests with pytest

Development workflow:

Feature Branch
→ Add Code
→ Run Tests
→ Pull Request
→ GitHub Actions CI
→ Merge to Main

## Testing

Run tests locally with:

```bash
python -m pytest

