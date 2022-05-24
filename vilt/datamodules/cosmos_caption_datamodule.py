from vilt.datasets import COSMOSCaptionDataset
from .datamodule_base import BaseDataModule


class COSMOSCaptionDataModule(BaseDataModule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def dataset_cls(self):
        return COSMOSCaptionDataset

    @property
    def dataset_cls_no_false(self):
        return COSMOSCaptionDataset

    @property
    def dataset_name(self):
        return "cosmos_caption"
