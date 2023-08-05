"""TODO(test_dataset_targz): Add a description here."""


import json
import datasets
# TODO: BibTeX citation
_CITATION = " "

_DESCRIPTION = "This is a dataset for testing the dataset builder script."

_URL = "https://github.com/snehangshuk/creating-hs-datasets/raw/main/00_get_started/dataset.tar.gz"


class test_dataset_targz(datasets.GeneratorBasedBuilder):
    def _info(self):
        # Specifies the datasets.DatasetInfo object
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # datasets.features.FeatureConnectors
            features=datasets.Features(
                {
                    "city": datasets.Value("string"),
                    "country": datasets.Value("string"),
                    "region": datasets.Value("string"),
                    "continent": datasets.Value("string"),
                    "latitude": datasets.Value("float64"),
                    "longitude": datasets.Value("float64"),
                    "x": datasets.Value("float64"),
                    "y": datasets.Value("float64"),
                    "z": datasets.Value("float64")
                }
            ),
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # Downloads the data and defines the splits
        # dl_manager is a datasets.download.DownloadManager that can be used to
        # download and extract URLs
        urls_to_download = _URL
        path = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(
             name=datasets.Split.TRAIN,
             gen_kwargs={"filepath": path+"/dataset.jsonl"}
            )
        ]

    def _generate_examples(self, filepath):
        """Yields examples."""
        # Yields (key, example) tuples from the dataset
        idx = 0
        # open json file and read line by line
        with open(filepath, encoding="utf-8") as fp:
            for line in fp:
                # load line as json object
                obj = json.loads(line)
                yield idx, obj
                idx += 1
