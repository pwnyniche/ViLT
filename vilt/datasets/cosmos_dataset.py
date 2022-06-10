from .base_dataset import BaseDataset
import sys
import random


class COSMOSDataset(BaseDataset):
    def __init__(self, *args, split="", **kwargs):
        assert split in ["train", "val", "test"]
        self.split = split

        if split == "train":
            names = ["cosmos_train"]
        elif split == "val":
            names = ["cosmos_val"]
        elif split == "test":
            names = ["cosmos_val"]

        super().__init__(
            *args,
            **kwargs,
            names=names,
            text_column_name="caption_1",
            remove_duplicate=True,
        )

    def get_text2(self, raw_index):
        index, caption_index = self.index_mapper[raw_index]
        text = self.table['caption_2'][index][0].as_py()

        encoding = self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.max_text_len,
            return_special_tokens_mask=True,
        )
        return {
            "text": (text, encoding),
            "img_index": index,
            "cap_index": caption_index,
            "raw_index": raw_index,
        }

    def __getitem__(self, index):
        result = None
        while result is None:
            # try:
            image_tensor = self.get_image(index, image_key="image")["image"]
            text = self.get_text(index)["text"]
            text2 = self.get_text2(index)["text"]
            result = True
            # except:
            #     print(
            #         f"error while read file idx {index} in {self.names[0]}",
            #         file=sys.stderr,
            #     )
            #     index = random.randint(0, len(self.index_mapper) - 1)

        index, question_index = self.index_mapper[index]
        answers = self.table["label"][index][question_index].as_py()
        # answers = answers == "True"

        return {
            "image": image_tensor,
            "text": text,
            "text2": text2,
            "answers": answers,
            "table_name": self.table_names[index],
        }
