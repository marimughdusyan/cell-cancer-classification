import numpy as np
import pickle
import pandas as pd
import glob
import matplotlib.pyplot as plt


# ── 1. DATA LOADING ──────────────────────────────────────────────────────

def load_pickle(path='specimens_toy_data.pkl'):
    with open(path, 'rb') as f:
        raw = pickle.load(f)

    images = {cat: raw[cat]['imgs'] for cat in raw}

    df = pd.concat(
        [raw[cat]['metadata'].assign(category=cat) for cat in raw],
        ignore_index=True
    )

    return images, df


def images_and_masks(folder='imagedata'):
    """Extract images and masks from a category"""

    # ── Load data ──────────────────────────────────────────────────────────────
    N = len(glob.glob(f'{folder}/X/*.npy'))
    X = np.stack([np.load(f'{folder}/X/{i}.npy') for i in range(N)])
    y = np.stack([np.load(f'{folder}/y/{i}.npy') for i in range(N)])

    # Drop images with no nucleus
    has_nucleus = (y == 2).sum(axis=(1, 2)) > 0
    X, y = X[has_nucleus], y[has_nucleus]

    return X, y

# ── 2. VISUALIZATION ─────────────────────────────────────────────────────
def show_image_mask(image, mask, pred = False):
    """Plot a cell image alongside its mask."""
    # Handle channels-first format (C, H, W) → (H, W, C)
    if pred == False:
        if image.ndim == 3 and image.shape[0] == 3:
            image = image.transpose(1, 2, 0)

        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        axes[0].imshow(image, cmap='gray' if image.ndim == 2 else None)
        axes[0].set_title('Cell Image')
        axes[0].axis('off')

        axes[1].imshow(mask, cmap='viridis', vmin=0, vmax=2)
        axes[1].set_title('Mask (0=bg, 1=cyto, 2=nucleus)')
        axes[1].axis('off')
    else:
        
    plt.tight_layout()
    plt.show()
#
# def show_prediction_vs_truth(image, predicted_mask, true_mask):
#     """Plot image | predicted mask | ground truth side by side"""
#
#
# # ── 4. EVALUATION METRICS ────────────────────────────────────────────────
# def dice_score(predicted_mask, true_mask):
#     """Compute Dice coefficient between two masks"""
#
#
# def iou_score(predicted_mask, true_mask):
#     """Compute Intersection over Union between two masks"""
#
#
# def evaluate_method(predicted_masks, true_masks, method_name):
#     """Run both metrics on all pairs and print a summary"""
#
#
# # ── 5. PREPROCESSING ─────────────────────────────────────────────────────
# def normalize_image(image):
#     """Normalize pixel values to [0, 1]"""
#
#
# def resize_pair(image, mask, size):
#     """Resize both image and mask to the same target size"""
#
#
# def binarize_mask(mask, threshold=0.5):
#     """Convert a soft/predicted mask to binary 0/1"""
