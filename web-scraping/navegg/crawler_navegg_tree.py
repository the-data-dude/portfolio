
import requests
import pandas as pd
from bs4 import BeautifulSoup


page = requests.get("https://www.navegg.com/segmentos/arvore-segmentos/?demo")
soup = BeautifulSoup(page.content, "html.parser")

segments = soup.find_all("div", class_ = "box-tree")
result_df = pd.DataFrame(columns = ['segment', 'type', 'sub_type', 'navegg_id', 'dv360_id', 'verizon_id', 'mediamath_id'])

for segment in segments:

    segment_id = segment.get("id")
    segment_div = soup.find("div", id = segment.get("id"))
    
    for sub_type in segment_div.find_all("h3"):
        segment_type = sub_type.text
        for sibling in sub_type.find_next_sibling():
            if sibling.name == "li":
                sibling_array = sibling.text.replace("ID", ":").replace("Navegg","").replace("DV360","").replace("Verizon","").replace("MediaMath","").replace(" ","").replace("::", ":").split(":")
                tmp = pd.DataFrame({'segment': segment_id,
                            'type': segment_type,
                            'sub_type': sibling_array[0],
                            'navegg_id': sibling_array[1],
                            'dv360_id': sibling_array[2],
                            'verizon_id': sibling_array[3],
                           'mediamath_id': sibling_array[4]}, index=[0])

                result_df = result_df.append(tmp)        


result_df.reset_index(drop = True).to_csv("navegg_tree.csv")
