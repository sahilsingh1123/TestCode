import tensorflow as tf
import torch

# if torch.backends.mps.is_available():
#     print("MPS is available for PyTorch on your Mac.")
# else:
#     print("MPS is not available on this device.")


physical_devices = tf.config.list_physical_devices("GPU")
if len(physical_devices) > 0:
    print(f"Number of GPUs available: {len(physical_devices)}")
    for device in physical_devices:
        print(device)
else:
    print("No GPU found. Running inference on CPU.")
