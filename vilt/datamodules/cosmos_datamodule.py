from vilt.datasets import COSMOSDataset
from .datamodule_base import BaseDataModule


class COSMOSDataModule(BaseDataModule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def dataset_cls(self):
        return COSMOSDataset

    @property
    def dataset_name(self):
        return "cosmos"
