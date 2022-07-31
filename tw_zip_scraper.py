from pyquery import PyQuery as pq
import json

class TaiwanZipScraper:
    def __init__(self):
        self.city_list = []
        self.zip_list = []
        self.zip_district = {}
        self.district_zip = {}
        self.city_district_list = {}
        self.city_zip_list = {}
        self.city_zip_full = {}
        self.city_district_full = {}
        self.full_list = []
        # scrape data
        self.scrape_data()
        # export json files
        self.export_city_list()
        self.export_zip_list()
        self.export_zip_district()
        self.export_district_zip()
        self.export_city_district_list()
        self.export_city_zip_list()
        self.export_city_district_full()
        self.export_city_zip_full()
        self.export_full_list()

    def scrape_data(self):
        # 臺灣地區郵遞區號一覽表
        url = "https://zh.m.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E5%9C%B0%E5%8D%80%E9%83%B5%E9%81%9E%E5%8D%80%E8%99%9F%E4%B8%80%E8%A6%BD%E8%A1%A8"
        html = pq(url)
        content_section_block = pq(html(".mf-section-4"))
        table_list = content_section_block("table")
        city_list = content_section_block("span.mw-headline>a").text().split()
        self.city_list = city_list
        for i, table in enumerate(table_list):
            table = pq(table)
            tr_list = table("tbody>tr:not(:first-child)")
            city = city_list[i]
            self.city_district_full[city] = {}
            self.city_zip_full[city] = {}
            self.city_district_list[city] = []
            self.city_zip_list[city] = []
            for tr in tr_list:
                tr = pq(tr)
                td_list = tr("td")
                for idx,td in enumerate(td_list):
                    if idx % 3 != 0:
                        continue
                    district_name = pq(td_list[idx]).text()
                    if "*" in district_name or len(district_name) < 1:
                        continue
                    zip = pq(td_list[idx+1]).text()
                    full_map = {"district_name": district_name, "zip_number": zip, "city_name": city}
                    self.city_district_full[city][district_name] = full_map
                    self.city_zip_full[city][zip] = full_map
                    self.zip_district[zip] = district_name
                    self.district_zip[district_name] = zip
                    self.zip_list.append(zip)
                    self.full_list.append(full_map)
                    self.city_district_list[city].append(district_name)
                    self.city_zip_list[city].append(zip)

    def export_json(self, file_name, data):
        with open(file_name + ".json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def export_city_list(self):
        self.export_json("city_list", self.city_list)

    def export_zip_list(self):
        self.export_json("zip_list", self.zip_list)

    def export_zip_district(self):
        self.export_json("zip_district", self.zip_district)

    def export_district_zip(self):
        self.export_json("district_zip", self.district_zip)

    def export_city_district_list(self):
        self.export_json("city_district_list", self.city_district_list)

    def export_city_zip_list(self):
        self.export_json("export_city_zip_list", self.city_zip_list)

    def export_city_district_full(self):
        self.export_json("city_district_full", self.city_district_full)

    def export_city_zip_full(self):
        self.export_json("city_zip_full", self.city_zip_full)

    def export_full_list(self):
        self.export_json("full_list", self.full_list)

# Create instance
taiwan_zip_scraper = TaiwanZipScraper()