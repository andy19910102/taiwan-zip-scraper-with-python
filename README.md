# Taiwan ZIP Scraper with Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Install the necessary Modules

```shell=
$ pip install pyquery
```

## Start scrape and generate data

```shell=
$ python tw_zip_scraper.py
```

## Export HTML with datatable.js

```python=
# Create instance
taiwan_zip_scraper = TaiwanZipScraper()

# Export HTML
taiwan_zip_scraper.export_html()
```

[Live Demo](https://andy19910102.github.io/taiwan-zip-scraper-with-python/taiwan_zip.html)

## Export formats

### city_district_full.json

```json=
{
    "臺北市": {
        "中正區": {
            "district_name": "中正區",
            "zip_number": "100",
            "city_name": "臺北市"
        },
        "大同區": {
            "district_name": "大同區",
            "zip_number": "103",
            "city_name": "臺北市"
        },
        "中山區": {
            "district_name": "中山區",
            "zip_number": "104",
            "city_name": "臺北市"
        },
        ...
    },
    ...
}
```

### city_district_list.json

```json=
{
    "臺北市": [
        "中正區",
        "大同區",
        "中山區",
        "松山區",
        "大安區",
        "萬華區",
        ...
    ],
    ...
}
```

### city_list.json

```json=
[
    "臺北市",
    "基隆市",
    "連江縣",
    "新北市",
    "宜蘭縣",
    ...
]
```

### city_zip_full.json

```json=
{
    "臺北市": {
        "100": {
            "district_name": "中正區",
            "zip_number": "100",
            "city_name": "臺北市"
        },
        "103": {
            "district_name": "大同區",
            "zip_number": "103",
            "city_name": "臺北市"
        },
        "104": {
            "district_name": "中山區",
            "zip_number": "104",
            "city_name": "臺北市"
        },
        "105": {
            "district_name": "松山區",
            "zip_number": "105",
            "city_name": "臺北市"
        },
        ...
    },
    ...
}
```

### city_zip_list.json

```json=
{
    "臺北市": [
        "100",
        "103",
        "104",
        "105",
        "106",
        "108",
        "110",
        "111",
        "112",
        ...
    ,
    ...
}
```

### district_full.json

```json=
{
    "中正區": {
        "district_name": "中正區",
        "zip_number": "202",
        "city_name": "基隆市"
    },
    "大同區": {
        "district_name": "大同區",
        "zip_number": "103",
        "city_name": "臺北市"
    },
    "中山區": {
        "district_name": "中山區",
        "zip_number": "203",
        "city_name": "基隆市"
    },
    ...
}
```

### district_list.json

```json=
[
    "中正區",
    "大同區",
    "中山區",
    "松山區",
    "大安區",
    "萬華區",
    "信義區",
    "士林區",
    "北投區",
    ...
]
```

### district_zip.json

```json=
{
    "中正區": "202",
    "大同區": "103",
    "中山區": "203",
    "松山區": "105",
    "大安區": "439",
    "萬華區": "108",
    "信義區": "201",
    "士林區": "111",
    "北投區": "112",
    "內湖區": "114",
    "南港區": "115",
    ...
}
```

### full_list.json

```json=
[
    {
        "district_name": "中正區",
        "zip_number": "100",
        "city_name": "臺北市"
    },
    {
        "district_name": "大同區",
        "zip_number": "103",
        "city_name": "臺北市"
    },
    {
        "district_name": "中山區",
        "zip_number": "104",
        "city_name": "臺北市"
    },
    ...
]
```

### zip_district.json

```json=
{
    "100": "中正區",
    "103": "大同區",
    "104": "中山區",
    "105": "松山區",
    "106": "大安區",
    "108": "萬華區",
    ...
}
```

### zip_fill.json

```json=
{
    "100": {
        "district_name": "中正區",
        "zip_number": "100",
        "city_name": "臺北市"
    },
    "103": {
        "district_name": "大同區",
        "zip_number": "103",
        "city_name": "臺北市"
    },
    "104": {
        "district_name": "中山區",
        "zip_number": "104",
        "city_name": "臺北市"
    },
    ...
}
```

### zip_list.json

```json=
[
    "100",
    "103",
    "104",
    "105",
    "106",
    "108",
    "110",
    "111",
    "112",
    ...
]
```

## Data source

All of these data are coming from  [維基百科 臺灣地區郵遞區號一覽表](https://zh.m.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E5%9C%B0%E5%8D%80%E9%83%B5%E9%81%9E%E5%8D%80%E8%99%9F%E4%B8%80%E8%A6%BD%E8%A1%A8)