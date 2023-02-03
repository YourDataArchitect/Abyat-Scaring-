import scrapy
import json 
import time 
from tabulate import tabulate
from scrapy.loader import ItemLoader
from ..items import AbyatItem
from scrapy.crawler import CrawlerProcess

class AbyatApiSpider(scrapy.Spider):
    name = 'abyat_api_new'
        
    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    'ROBOTSTXT_OBEY' : False,
    'DOWNLOAD_DELAY' : 1,
    'CONCURRENT_REQUESTS' : 15,
    'FEED_EXPORTERS' : {'xlsx': 'scrapy_xlsx.XlsxItemExporter'},
    'COOKIES_ENABLED' : False,
    'DOWNLOADER_MIDDLEWARES' : {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None}}
    
    
    
    

    print('               ██      ▄██                           ██')   
    print('              ▄██▄      ██                           ██ ')  
    print('             ▄█▀██▄     ██▄████▄ ▀██▀   ▀██▀▄█▀██▄ ██████') 
    print('            ▄█  ▀██     ██    ▀██  ██   ▄█ ██   ██   ██   ')
    print('            ████████    ██     ██   ██ ▄█   ▄█████   ██   ')
    print('           █▀      ██   ██▄   ▄██    ███   ██   ██   ██   ')
    print('         ▄███▄   ▄████▄ █▀█████▀     ▄█    ▀████▀██▄ ▀████')
    print('                                    ▄█                     ')
                                                                              
      
    
    data =  [[1,'Plants',51,'  Kitchen Utensils'],
    [2,'Outdoor Accessories',52,'Kitchen Storages'],
    [3,'Dining Tables',53,'Drinkware'],
    [4,'Wallpaper',54,'  Dinnerware'],
    [5,'Wall Cladding',55,' Cutleries'],
    [6,'Decorative Elements',56,'  Roll Curtains'],
    [7,' Wall Art',57,'  Ready Made Curtains'],
    [8,'Painted and Printed Art',58,' Lanterns'],
    [9,' Hanging Frames',59,'Home Fragrances'],
    [10,' Clocks',60,' Night stands'],
    [11,' Wood Texture Floor',61,' Mattresses'],
    [12,' Wall Tiles',62,' Chairs'],
    [13,' Stairs',63,' Beds'],
    [14,' Profiles',64,'Counter top Bath Accessories'],
    [15,'Outdoor Floor',65,' Clothes Racks'],
    [16,'  Mosaic',66,'  Bedding Basics'],
    [17,' Floor Tiles',67,' Bathroom Mirrors'],
    [18,' Office Chairs',68,'Sanitary Ware'],
    [19,'  Desks',69,'  Sanitary Fittings'],
    [20,'  Home Storages',70,'  Plumbing Accessories'],
    [21,'  Rugs',71,'Mirrors'],
    [22,'KidsRugs',72,' Bathtubs'],
    [23,'  Parquet',73,'Bathroom Furniture'],
    [24,' SunLoungers',74,' Bathroom Accessories'],
    [25,'Outdoor Seating',75,'Adhesive Grout'],
    [26,' Outdoor Dining',76,' Babies Bedding Bath'],
    [27,' Gazebos',77,'  Bar Tables Counter Stools'],
    [28,' Tables',78,'  Bathroom Sets Holders Essentials'],
    [29,' Sofas',79,' Blanket Throws'],
    [30,'  Cabinets',80,' Bookcases Shelves'],
    [31,'Wiring Accessories',81,'  Buffets Sideboards'],
    [32,' SurfaceMount',82,' Candles Candle Holders'],
    [33,'  RecessedMount',83,'Chests Dressers'],
    [34,' Outdoor Lighting',84,' Coat Hanger Shoe Racks'],
    [35,'LED Strip and Fiber',85,' Decorative Floor Pillows'],
    [36,' Electrical Accessories',86,' Flowers Leaves'],
    [37,' Decorative Lighting',87,' Jewelry Organization Boxes'],
    [38,' Chandelier',88,'Ornaments Photo Frames'],
    [39,' Bulbs',89,'Pots Planters'],
    [40,'  Bedroom',90,'  Shower Tray Enclosures'],
    [41,' School Essentials',91,'Study Play Room'],
    [42,'  Outdoors Essentials',92,'  Tea Coffee'],
    [43,' Organization Essentials',93,' Towels Mats Bathrobes'],
    [44,' Living Rooms Essentials',94,' Toys Play Room Accessories'],
    [45,' Kitchen Essentials',95,' Trays Trolleys'],
    [46,' Dining Essentials',96,' TV Stands Wall Units'],
    [47,'  Baths Essentials',97,'Vases Planters]'],
    [48,'Dining Room Sets',98,'All Products'],
    [49,'Dining Chairs',''],
    [50,'  Serveware','']
    ]
    print (tabulate(data, headers=['Key','category','Key' , 'category']))
    time.sleep(5)
    
   
    variants_dict= {}
    
    def start_requests(self):
        sub_catagories_list = ['Plants'	,'Outdoor Accessories',	'Dining Tables',	'Wallpaper',	'Wall Cladding',	'Decorative Elements',	'Wall Art',	'Painted and Printed Art',	'Hanging Frames',	'Clocks',	'Wood Texture Floor',	'Wall Tiles',	'Stairs',	'Profiles',	'Outdoor Floor',	'Mosaic',	'Floor Tiles',	'Office Chairs',	'Desks',	'Home Storages',	'Rugs',	'Kids Rugs',	'Parquet',	'Sun Loungers',	'Outdoor Seating',	'Outdoor Dining',	'Gazebos',	'Tables',	'Sofas',	'Cabinets',	'Wiring Accessories',	'Surface Mount',	'Recessed Mount',	'Outdoor Lighting',	'LED Strip and Fiber',	'Electrical Accessories',	'Decorative Lighting',	'Chandelier',	'Bulbs',	'Bedroom',	'School Essentials',	'Outdoors Essentials',	'Organization Essentials',	'Living Rooms Essentials',	'Kitchen Essentials',	'Dining Essentials',	'Baths Essentials',	'Dining Room Sets',	'Dining Chairs',	'Serveware',	'Kitchen Utensils',	'Kitchen Storages',	'Drinkware',	'Dinnerware',	'Cutleries',	'Roll Curtains',	'Ready Made Curtains',	'Lanterns',	'Home Fragrances',	'Nightstands',	'Mattresses',	'Chairs',	'Beds',	'Countertop Bath Accessories',	'Clothes Racks',	'Bedding Basics',	'Bathroom Mirrors',	'Sanitary Ware',	'Sanitary Fittings',	'Plumbing Accessories',	'Mirrors',	'Bathtubs',	'Bathroom Furniture',	'Bathroom Accessories',	'Adhesive%20%26%20Grout',	'Babies%20Bedding%20%26%20Bath',	'Bar%20Tables%20%26%20Counter%20Stools',	'Bathroom%20Sets%2C%20Holders%20%26%20Essentials',	'Blanket%20%26%20Throws',	'Bookcases%20%26%20Shelves',	'Buffets%20%26%20Sideboards',	'Candles%20%26%20Candle%20Holders',	'Chests%20%26%20Dressers',	'Coat%20Hanger%20%26%20Shoe%20Racks',	'Decorative%20%26%20Floor%20Pillows',	'Flowers%20%26%20Leaves',	'Jewelry%20%26%20Organization%20Boxes',	'Ornaments%20%26%20Photo%20Frames',	'Pots%20%26%20Planters',	'Shower%20Tray%20%26%20Enclosures',	'Study%20%26%20Play%20Room',	'Tea%20%26%20Coffee',	'Towels%2C%20Mats%20%26%20Bathrobes',	'Toys%20%26%20Play%20Room%20Accessories',	'Trays%20%26%20Trolleys',	'TV%20Stands%20%26%20Wall%20Units',	'Vases%20%26%20Planters']
        sub_catagories_pages = [5,3,2,13,2,2,2,4,2,1,2,6,1,1,1,2,5,1,1,5,3,1,4,1,2,2,1,4,4,1,4,2,2,3,1,1,6,4,1,3,2,1,2,1,1,2,1,1,2,6,3,3,3,8,3,8,1,2,3,2,2,1,2,2,1,9,1,3,5,2,2,1,2,5,1,1,1,2,2,2,1,7,2,2,8,3,3,2,4,1,1,6,2,2,4,2,4]
        key = int(input ('Please Enter category Key :'))
        if key == 98 :
            for i in range(len(sub_catagories_list)):  
                range_pages = sub_catagories_pages[i]+1
                print(sub_catagories_list[i])
                for page in range (range_pages):
                    link_api = f'https://api.abyat.com/search/?locale=ar-SA&currency=SAR&page={page+1}&size=48&marketplace=SA&subCategory={sub_catagories_list[i]}'
                    try : 
                        yield scrapy.Request(url=link_api,
                                        callback=self.parse_sub_catagory_page)
                    except :
                        print(f"--------------------{link_api}")
                    pass
        else : 
            range_pages = sub_catagories_pages[key-1]     
            key_catagory = sub_catagories_list[key-1]
            

            for page in range (range_pages):              
                link_api = f'https://api.abyat.com/search/?locale=ar-SA&currency=SAR&page={page+1}&size=48&marketplace=SA&subCategory={sub_catagories_list[key-1]}'
                print('key ------------> ',key)

   
                try : 
                    yield scrapy.Request(url=link_api,
                                    callback=self.parse_sub_catagory_page,
                                    meta = {'key_catagory':key_catagory})



                except :
                    print(f"--------------------{link_api}")
                    pass
            

    def parse_sub_catagory_page(self, response):
        # key = response.meta.get('key')
        key_catagory = response.meta.get('key_catagory')
 

        # time.sleep(2)
        data = json.loads(response.body)
        list_linid = []
        for item in data['hits']:
            yield list_linid.append(item['lineId'])
        for id in list_linid:
            for page_number in range (1,4):   
                yield response.follow(url = f'https://api.abyat.com/search/?locale=ar-SA&currency=SAR&page={page_number}&size=48&marketplace=SA&lineID={id}',
                                callback = self.parse_lineid,
                                meta = {'key_catagory':key_catagory})






    def parse_lineid(self,response):
        # key = response.meta['key']
        # key = response.meta.get('key')

        key_catagory = response.meta['key_catagory'] 
        print('-------------> the key catagory : ',key_catagory)
        productid_list = [] 
        time.sleep(2)        
        data = json.loads(response.body)
        for item in data['hits']:
            print('-----------item["subCategory"]--------------------->>>>>>>>',item['subCategoryId'])
            # if item['subCategoryId'] == key_catagory and key != 98: # original
            if item['subCategoryId'] == key_catagory :    
                yield productid_list.append(item['productId'])     
            if  key_catagory == None: 
                yield productid_list.append(item['productId'])
                              
        for product_id in productid_list : 
        # for product_id in productid_list :     
            yield response.follow(url = f'https://api.abyat.com/products/{product_id}?locale=ar-SA&currency=SAR&marketplace=SA&withInstallation=true&forDisplay=true',
                callback = self.products_page_parse_arabic , meta = {'product_id' : product_id}) # the description is wrong 
    
    
    #448103
    def products_page_parse_arabic(self, response):
        # print(response.body)
        product_id = response.meta['product_id']
        time.sleep(2)
        data = json.loads(response.body)
        l = ItemLoader(item=AbyatItem(), selector=data)
        
        
        
        try : l.add_value('Arabic_Description', data['description'])
        except : pass
        try : l.add_value('Arabic_Name', data['title'])
        except : pass
        try :l.add_value('Arabic_Care_Instructions_general' , data['careInstructions'].get('general'))
        except : pass
        try :l.add_value('Arabic_Care_Instructions_washing' , data['careInstructions'].get('washing'))
        except : pass
        try :l.add_value('Arabic_Care_Instructions_drying' , data['careInstructions'].get('drying'))
        except : pass
        try :l.add_value('Arabic_Care_Instructions_disclaimer' , data['careInstructions'].get('disclaimer'))
        except : pass
        try :l.add_value('Arabic_categoryId' , data['category'] )
        except : pass
        try :l.add_value('Arabic_subCategoryId' , data['subCategory'])
        except : pass
        try :l.add_value('Arabic_color' , data['color'])
        except : pass
        try :l.add_value('Arabic_category' , data['merchandiseCategory'])
        except : pass
        try :l.add_value('Arabic_countryOfOrigin' , data['countryOfOrigin'])
        except : pass
        try :l.add_value('Arabic_dimension' , data['dimension'].get('dimension')) 
        except : pass
        try :l.add_value('Arabic_length' , data['dimension'].get('length'))
        except : pass
        try :l.add_value('Arabic_width' , data['dimension'].get('width'))
        except : pass
        try :l.add_value('Arabic_height' , data['dimension'].get('height'))
        except : pass
        try :l.add_value('Arabic_unit' , data['dimension'].get('unit'))
        except : pass

        try :l.add_value('Arabic_grossWeight' , data['grossWeight'].get('grossWeight'))
        except : pass
        
        try :l.add_value('Arabic_finish' , data['finish'])
        except : pass
        try :l.add_value('Arabic_style' , data['style'])
        except : pass
        try :l.add_value('Arabic_shape' , data['shape'])
        except : pass
        try : l.add_value('Arabic_materials' , data['materials'])
        except : pass
        try : l.add_value('Arabic_Category' , str(data['title'] + ' & ' + str(data['merchandiseCategory']) + ' & ' +str(data['subCategory'])+ ' & ' + str(data['category'])  ))
        except : pass
        try : l.add_value('Arabic_stock' , data['productAvailability'].get('stock').get('RY'))
        except : pass





        # yield l.load_item()
        # for product_id in productid_list : 
        yield response.follow(url = f'https://api.abyat.com/products/{product_id}?locale=en-US&currency=SAR&marketplace=SA&withInstallation=true&forDisplay=true',
            callback = self.products_page_parse , meta = {'l' : l}) # the description is wrong 
        
            

    def products_page_parse(self,response):
        l = response.meta['l']
        time.sleep(2)

        data = json.loads(response.body)
        try :l.add_value('SKU', data['productId'])   
        except : pass
        try :l.add_value('English_Name' , data['title'])
        except : pass
        try :l.add_value('Price' , data['price'].get('amount'))
        except : pass
        try :l.add_value('English_Description' , data['description'])
        except : pass
        try :l.add_value('Care_Instructions_general' , data['careInstructions'].get('general'))
        except : pass
        try :l.add_value('Care_Instructions_washing' , data['careInstructions'].get('washing'))
        except : pass
        try :l.add_value('Care_Instructions_drying' , data['careInstructions'].get('drying'))
        except : pass
        try :l.add_value('Care_Instructions_disclaimer' , data['careInstructions'].get('disclaimer'))
        except : pass
        try :l.add_value('categoryId' , data['categoryId'] )
        except : pass
        try :l.add_value('subCategoryId' , data['subCategoryId'])
        except : pass
        try :l.add_value('color' , data['color'])
        except : pass
        try :l.add_value('category' , data['category'])
        except : pass
        try :l.add_value('countryOfOrigin' , data['countryOfOrigin'])
        except : pass
        try :l.add_value('dimension' , data['dimension'].get('dimension')) 
        except : pass
        try :l.add_value('length' , data['dimension'].get('length'))
        except : pass
        try :l.add_value('width' , data['dimension'].get('width'))
        except : pass
        try :l.add_value('height' , data['dimension'].get('height'))
        except : pass
        try :l.add_value('unit' , data['dimension'].get('unit'))
        except : pass
        try :l.add_value('productImages' , data['images'].get('productImages'))
        except : pass
        try :l.add_value('grossWeight' , data['grossWeight'].get('grossWeight'))
        except : pass
        try : l.add_value('landscape' , data['images'].get('lifestyleImages')[0].get('landscape'))
        except : pass   
        try : l.add_value('sizeImages' , data['images'].get('sizeImages'))
        except : pass 
        try :l.add_value('finish' , data['finish'])
        except : pass
        try :l.add_value('style' , data['style'])
        except : pass
        try :l.add_value('shape' , data['shape'])
        except : pass
        try :l.add_value('isHandmade' , data['isHandmade'])
        except : pass 
        try : l.add_value('numberOfPieces', data['numberOfPieces'][0])
        except : pass
        try : l.add_value('Installation_Price',data['deliveryPrice'])
        except : pass  
        try : l.add_value('materials' , data['materials'])
        except : pass
        try : l.add_value('Category' , str(data['categoryId']) + ' & ' +str(data['subCategoryId'])+ ' & ' + str(data['merchandiseCategory'])+ ' & ' + str(data['title']))
        except : pass
        try : l.add_value('stock' , data['productAvailability'].get('stock').get('RY'))
        except : pass
        try : l.add_value('Manufacturer' , data['articleGroupId'])
        except : pass
        


        if str(data['variantId'])+str(data['title']) not in AbyatApiSpider.variants_dict : 
            AbyatApiSpider.variants_dict[str(data['variantId'])+str(data['title'])] = data['title']
            l.add_value('Parent' , data['title'])            
        else : 
            l.add_value('Parent' ,AbyatApiSpider.variants_dict[str(data['variantId'])+str(data['title'])]) # the last order 

        print(AbyatApiSpider.variants_dict)
            
        try : l.add_value('variantId' , data['variantId'])
        except : pass
            
        

        yield l.load_item()
            
       
        
        
        