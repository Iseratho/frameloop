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
amr_graphs = fs(news_df["title"].tolist(), error_type=penman.decode("(amr-error)"))
structure_df = pd.DataFrame(list(map(penman.encode, amr_graphs)), index=news_df.index)
structure_df.to_csv("framestructure.csv", header=None)

news_df_with_abstracts = news_df.dropna(subset="abstract")

labels_abstracts_df = pd.DataFrame(fl(news_df_with_abstracts["abstract"].tolist()), index=news_df_with_abstracts.index)
labels_abstracts_df.to_csv("framelabelsA.csv")

dimensions_abstracts_df = pd.DataFrame(fd(news_df_with_abstracts["abstract"].tolist()), index=news_df_with_abstracts.index)
dimensions_abstracts_df.to_csv("framedimensionsA.csv")

amr_graphs_abstracts = fs(news_df_with_abstracts["abstract"].tolist(), error_type=penman.decode("(amr-error)"))
structure_abstracts_df = pd.DataFrame(list(map(penman.encode, amr_graphs_abstracts)), index=news_df_with_abstracts.index)
structure_abstracts_df.to_csv("framestructureA.csv", header=None)
