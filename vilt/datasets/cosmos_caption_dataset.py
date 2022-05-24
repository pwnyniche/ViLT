from .base_dataset import BaseDataset


class COSMOSCaptionDataset(BaseDataset):
    def __init__(self, *args, split="", **kwargs):
        assert split in ["train", "val", "test"]

        if split == "train":
            names = ["cosmos_train", "cosmos_val"]
        elif split == "val":
            names = ["cosmos_test"]
        elif split == "test":
            names = ["cosmos_test"]

        super().__init__(*args, **kwargs, names=names, text_column_name="caption")

    def __getitem__(self, index):
        return self.get_suite(index)
