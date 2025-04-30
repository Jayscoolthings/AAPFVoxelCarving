import h5py
import numpy as np

def update_learning_rate(model_path):
    """
    Attempts to update 'lr' to 'learning_rate' in a Keras .h5 model file.

    Args:
        model_path (str): Path to the .h5 model file.
    """
    try:
        with h5py.File(model_path, 'r+') as f:  # Open for read and write
            # Iterate through groups in the HDF5 file
            for name, group in f.items():
                if isinstance(group, h5py.Group):
                    # Check if the group contains an attribute named 'lr'
                    if 'lr' in group.attrs:
                        print(f"Found 'lr' attribute in group '{name}'.  Updating...")
                        group.attrs['learning_rate'] = group.attrs['lr'] # Copy value, rename key
                        del group.attrs['lr'] # Delete the old lr key

            print("Learning rate parameter updated (if found).")

    except Exception as e:
        print(f"Error updating learning rate: {e}")


# Usage:
model_path = 'sorghum_segmentation_model_cnn715_2000_epochs.h5'
update_learning_rate(model_path)
