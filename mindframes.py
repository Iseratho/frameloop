# %pip install framefinder sentence_transformers penman

import pandas as pd
from framefinder import examples
from framefinder import framelabels
from framefinder import framedimensions
from framefinder import framestructure
import penman

QUICK_RUN = False

news_df = pd.read_csv("news.tsv", sep="\t", header=None, index_col=0, names=["category", "subcategory", "title", "abstract", "link", "title_entities", "abstract_entities"])
if QUICK_RUN:
    news_df = news_df.head()

fl = framelabels.FramingLabels("facebook/bart-large-mnli", examples.candidate_labels)
labels_df = pd.DataFrame(fl(news_df["title"].tolist()), index=news_df.index)
labels_df.to_csv("framelabels.csv")

fd = framedimensions.FramingDimensions("all-mpnet-base-v2", examples.dimensions, examples.pole_names)
dimensions_df = pd.DataFrame(fd(news_df["title"].tolist()), index=news_df.index)
dimensions_df.to_csv("framedimensions.csv")

fs = framestructure.FramingStructure("Iseratho/model_parse_xfm_bart_base-v0_1_0")
structure_df = pd.DataFrame(list(map(penman.encode, fs(news_df["title"].tolist()))), index=news_df.index)
structure_df.to_csv("framestructure.csv", header=None)
