import pprint


arr_photos = ["https://img.fonwall.ru/o/aa/mr-freeman-mister-frimen-personazh-solnce.jpg",
              "https://coub-attachments.akamaized.net/coub_storage/coub/simple/cw_image/fd18d3a6f73/da1f1ba71159eb6da81ff/1499003203_00031.jpg",
              "https://i.ytimg.com/vi/43R4XZQoFrQ/maxresdefault.jpg",
             ]

photos = dict(zip(arr_photos, ['1', '2', '3']))

pprint.pprint(photos)
