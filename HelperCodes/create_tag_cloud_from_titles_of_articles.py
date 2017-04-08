from ReviewHelper import *

def main():


    list_of_journals = find_list_of_journals()

    full_list_of_articles = []

    for l in list_of_journals:
        base_file_name = find_input_file_name(l)

        file_content = read_tex_file_content(base_file_name)
        bibtex_file_content = read_bibtex_file_bibtex_directory_content(base_file_name)
        list_of_articles = re.findall("input.*", file_content)

        #print(base_file_name)
        #print(list_of_articles)

        for str_input_article in list_of_articles:
            bibtex_key = find_bibtex_key(str_input_article)
            #print(bibtex_key)
            #title = find_title(base_file_name,bibtex_key)
            #print(title)
            authors = find_authors(base_file_name,bibtex_key)
            print(authors)

if __name__ == "__main__":
    main()
    #title = find_title("TheScientificWorldJournal","Kumar2013Design")
    #print(title)









