from __future__ import print_function
import re
import codecs
import operator
import csv
import glob
import re
from os import listdir
from os.path import isfile, join
import pandas as pd


META_STARTS = "META_STARTS"
META_ENDS = "META_ENDS"
CONSTANT_ARTICLE = "@Article"

BIBTEX_MAIN_FILE_NAME = "KDD99ReviewArticles.bib"


bibtex_folder = "../../../latexAndBibliography/"


csv_save_folder = "../latex/excel/"


def get_csv_save_folder():
    return csv_save_folder


def read_file_return_content(file_name):
    f = codecs.open(file_name, "r", "utf-8") 
    c =  f.read()
    return c

def get_bibtex_full_filename_in_bibtex_directory(base_file_name):
    file_name = join(bibtex_folder, base_file_name) 
    return file_name

def read_bibtex_file_bibtex_directory_content(base_file_name):
    bibtex_file_name = get_bibtex_full_filename_in_bibtex_directory(base_file_name)
    bibtex_file_content = read_file_return_content(bibtex_file_name)
    return bibtex_file_content




def find_list_of_bib_files():
    files_to_find = bibtex_folder + "/*.bib"
    onlyfiles = [f for f in listdir(bibtex_folder) if isfile(join(bibtex_folder, f))]
    
    return [f for f in onlyfiles if f.endswith(".bib")]
    

    
def find_bibtex_entries_from_content(bib_file_content):
    article_list = bib_file_content.split(CONSTANT_ARTICLE)

    articles_containing_meta = []

    for article in article_list:
        if META_STARTS in article:
            articles_containing_meta.append(CONSTANT_ARTICLE + article)
    
    return articles_containing_meta
        
             



def combine_bib_files_in_latexAndBibliography_to_one_list():
    all_articles = []
    total_article_count = 0
    list_of_bib_files = sorted(find_list_of_bib_files())
    journal_count = 0
    for bib_filename in list_of_bib_files:
        bib_file_content = read_bibtex_file_bibtex_directory_content(bib_filename)
        if META_STARTS in bib_file_content:
            journal_count = journal_count + 1
            
            list_of_articles_from_bib_file = find_bibtex_entries_from_content(bib_file_content)
            all_articles = all_articles + list_of_articles_from_bib_file
            journal_article_count = len(list_of_articles_from_bib_file)
            print(bib_filename)
            print("journal_article_count",journal_article_count)
            for article in list_of_articles_from_bib_file:
                first_line = article.split("\n")[0]
                print("\t\t",first_line)
            total_article_count = total_article_count + journal_article_count

    print("total_article_count",total_article_count)
    print("journal_count",journal_count)
    return all_articles


def create_kdd99_review_bib_file():
    list_of_all_articles = combine_bib_files_in_latexAndBibliography_to_one_list()
    fileToWrite = open(BIBTEX_MAIN_FILE_NAME, 'w')
    for bibtex_content in list_of_all_articles:
        lines = bibtex_content.split("\n")
        for line in lines:
            lineToWrite = not (("file" in line) or ("owner" in line) or ("@Comment" in line) or ("__markedentry" in line) or ("timestamp" in line) )
            if(lineToWrite):
                lineUtf8 = line.encode('utf-8')
                fileToWrite.write("%s\n" % lineUtf8)

    fileToWrite.close()



import bibtexparser

def get_list_of_dictionary_created_from_bibtex_file():
    
    with open(BIBTEX_MAIN_FILE_NAME) as bibtex_file:
        list_of_article_dictionaries = bibtexparser.load(bibtex_file)    
    
    
    for article_entry in list_of_article_dictionaries.entries:
        str_review = article_entry["review"]
        start = str_review.index("META_STARTS") 
        end = str_review.index("META_ENDS")
        meta_all_values = str_review[start:end]
        meta_lines = meta_all_values.split("\n")
        for meta_line in meta_lines:
            l = meta_line.split(":")
            if (len(l) > 1):
                (meta_name,meta_value) = (l[0],l[1]) 
                meta_name = meta_name.replace("%","").replace("-","").strip()
                meta_value = meta_value.strip()
                article_entry[meta_name] = meta_value

            
        
        
        
    return list_of_article_dictionaries

def get_pandas_data_frame_created_from_bibtex_file():
    list_of_all_articles = get_list_of_dictionary_created_from_bibtex_file()
    df = pd.DataFrame(list_of_all_articles.entries)
    return df



def get_pandas_data_frame_dataset_sizes_training():

    df = get_pandas_data_frame_created_from_bibtex_file()

    # find wrong records
    # df[df.metaTrainingSetSizes.isnull()].ID

    list1 = df.metaTrainingSetSizes.str.split(",").tolist()

    temp_list = []

    for inner_list in list1:
        for test_size in inner_list:
            try:
                a = int(test_size)
                temp_list.append(a)
            except:
                pass

    list2 = sorted(temp_list)

    df1 = pd.DataFrame(list2)
    return df1

def get_pandas_data_frame_dataset_sizes_testing():

    df = get_pandas_data_frame_created_from_bibtex_file()

    # find wrong records
    # df[df.metaTestSetSizes.isnull()].ID


    list1 = df.metaTestSetSizes.str.split(",").tolist()

    temp_list = []

    for inner_list in list1:
        for test_size in inner_list:
            try:
                a = int(test_size)
                temp_list.append(a)
            except:
                pass

    list2 = sorted(temp_list)

    df1 = pd.DataFrame(list2)
    return df1

def get_other_dataset_usage_count(dataset_name):
    df = get_pandas_data_frame_created_from_bibtex_file()
    usage_count = df.metaDatasetsUsed.str.contains(dataset_name).sum()
    return usage_count




def get_other_ids_datasets_usage_count_apart_from_darpa():
    iscx_count = get_other_dataset_usage_count("ISCX")
    kyoto_count = get_other_dataset_usage_count("Kyoto")
    return iscx_count + kyoto_count



if __name__ == "__main__":
    create_kdd99_review_bib_file()
    #list_of_all_articles = get_list_of_dictionary_created_from_bibtex_file()
    #print(list_of_all_articles.entries)
    