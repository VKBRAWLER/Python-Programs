import cv2
import numpy as np

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

# Example usage:
img1 = cv2.imread('q.jpg')
img2 = cv2.imread('r.jpg')
mse_value = mse(img1, img2)
print(f"Mean Squared Error: {mse_value:.2f}")
