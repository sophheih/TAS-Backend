def generically_filter(something, include): 
    results = list() 
    for each in something: 
        if each in include: 
            results.append(each)
         
    return results 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from otherRest_api.serializer import constMenuSerializer
from dish_api.serializer import DishSerializer
from TASBackend.models import constantMenu
from TASBackend.models import dish
from mongoengine.errors import ValidationError
import datetime
def checkDishExisted(dishName):
    try: 
        d = dish.objects.get(Name = dishName)
    except dish.DoesNotExist:
        return False
    except ValidationError:
        return False
    except:
        return False

    return d.id

def saveDish(dishName, totalcal, totalFat, cholesterol, sodium, totalCarbs, protein, index):
    _id = checkDishExisted(dishName)

    print()
    print("-------> dish name: {}, _id; {}".format(dishName, _id))

    if _id:
        return str(_id)

    if dishName is None:
        return False
    if totalcal is None:
        return False
    if totalFat is None:
        return False
    if cholesterol is None:
        return False
    if sodium is None:
        return False
    if totalCarbs is None:
        return False
    if protein is None:
        return False
    if index is None:
        return False
    # if timestamp is None:
    #     return False
    
    serializer = DishSerializer(data = { 
        'Name':str(dishName),
        'Calories': int(totalcal),
        'Total_Fat': float(totalFat),
        'Cholesterol': int(cholesterol),
        'Sodium': int(sodium),
        'Total_Carbs' : int(totalCarbs),
        'Protein': int(protein),
        'Index': int(index),
        # 'Timestamp': int(timestamp),
    }) 
    if serializer.is_valid():
        serializer.save()
    
    __id = checkDishExisted(dishName)
    while __id is False:
        __id = checkDishExisted(dishName)
    print("xxxx> dish name: {}, __id; {}".format(dishName, __id))

    if __id:
        return str(__id)

def checkMenuExisted(name):
    try:
        menu = constantMenu.objects.get(RestName = name)
    except constantMenu.DoesNotExist:
        return False
    except ValidationError:
        return False
    except:
        return False
    
    return True
def saveConstMenu(restName, food):
    if restName is None:
        return False
    if checkMenuExisted(restName) is False:
        return False
    if date is None:
        return False
    if food is None:
        return False
    
    # serializer makes sure input data is changed to readable type
    serializer = constMenuSerializer(data = { 
    
        'RestName': restName,
        'Date': date,
        'Side': side,
        'Fruit': fruit,
        
    }) 

    if serializer.is_valid():
        serializer.save()


def crawler():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')

    # driver = webdriver.Chrome(chrome_options = options, executable_path = "/Users/christianlin/Desktop/Coding/chromedriver")
    driver = webdriver.Chrome("/Users/22berniec/Desktop/chromedriver_win32/chromedriver")
    driver.get("https://tas.nutrislice.com/menu/tas/serving-line/print-menu/month/2021-04-16")   

    wait = WebDriverWait(driver, 20)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")))

    button = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")
    button.click()

    wait = WebDriverWait(driver, 20)
    wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "/html/body/div/ng-view/div/print-sidebar/div/div[1]/div[3]/div[1]/ul/li[1]/a")))

    body = driver.find_element(By.XPATH, "/html/body") 
    weekBlock = body.find_elements_by_xpath('//*[@class="menu-day-contents font-normal height11"]')
    print("weekBlock count: ", len(weekBlock))
    # /html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[1]/label/span
    button = body.find_element(By.TAG_NAME, "div")
    button = button.find_element(By.TAG_NAME, "ng-view")
    landscape = button.find_element(By.TAG_NAME, "div")
    printSidebar = landscape.find_element(By.TAG_NAME, "print-sidebar")
    button = printSidebar.find_element(By.CLASS_NAME, "rb")
    button = button.find_element(By.CLASS_NAME, "lists")
    button = button.find_element(By.TAG_NAME, "div")
    buttonList = button.find_element(By.TAG_NAME, "div")
    '''select calories button'''
    button = buttonList.find_element(By.TAG_NAME, "div")
    button = button.find_element(By.TAG_NAME, "label")
    button = button.find_element(By.TAG_NAME, "span")
    button.click()
    '''select carbohydrates button'''
    #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[2]/label/span 
    button = buttonList.find_elements(By.TAG_NAME, "div")[1]
    button = button.find_element(By.TAG_NAME, "label")
    button = button.find_element(By.TAG_NAME, "span")
    button.click()
    '''select Protein button'''
    #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[4]/label/span
    button = buttonList.find_elements(By.TAG_NAME, "div")[3]
    button = button.find_element(By.TAG_NAME, "label")
    button = button.find_element(By.TAG_NAME, "span")
    button.click()

    def secondSelectionStatus():
        body = driver.find_element(By.XPATH, "/html/body") 
        weekBlock = body.find_elements_by_xpath('//*[@class="menu-day-contents font-normal height11"]')
        # print("weekBlock count: ", len(weekBlock))
        # /html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[1]/label/span
        button = body.find_element(By.TAG_NAME, "div")
        button = button.find_element(By.TAG_NAME, "ng-view")
        landscape = button.find_element(By.TAG_NAME, "div")
        printSidebar = landscape.find_element(By.TAG_NAME, "print-sidebar")
        button = printSidebar.find_element(By.CLASS_NAME, "rb")
        button = button.find_element(By.CLASS_NAME, "lists")
        button = button.find_element(By.TAG_NAME, "div")
        buttonList = button.find_element(By.TAG_NAME, "div")
        '''deselect calories'''
        button = buttonList.find_element(By.TAG_NAME, "div")
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''deselect carbohydrates button'''
        #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[2]/label/span 
        button = buttonList.find_elements(By.TAG_NAME, "div")[1]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''deselect Protein button'''
        #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[4]/label/span
        button = buttonList.find_elements(By.TAG_NAME, "div")[3]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        '''select totalFat'''
        button = buttonList.find_elements(By.TAG_NAME, "div")[4]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''select cholesterol button'''
    
        button = buttonList.find_elements(By.TAG_NAME, "div")[7]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''select sodium button'''
        
        button = buttonList.find_elements(By.TAG_NAME, "div")[8]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
    def firstSelectionStatus():
        body = driver.find_element(By.XPATH, "/html/body") 
        weekBlock = body.find_elements_by_xpath('//*[@class="menu-day-contents font-normal height11"]')
        # print("weekBlock count: ", len(weekBlock))
        # /html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[1]/label/span
        button = body.find_element(By.TAG_NAME, "div")
        button = button.find_element(By.TAG_NAME, "ng-view")
        landscape = button.find_element(By.TAG_NAME, "div")
        printSidebar = landscape.find_element(By.TAG_NAME, "print-sidebar")
        button = printSidebar.find_element(By.CLASS_NAME, "rb")
        button = button.find_element(By.CLASS_NAME, "lists")
        button = button.find_element(By.TAG_NAME, "div")
        buttonList = button.find_element(By.TAG_NAME, "div")
        '''deselect totalFat'''
        button = buttonList.find_elements(By.TAG_NAME, "div")[4]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''deselect cholesterol button'''
    
        button = buttonList.find_elements(By.TAG_NAME, "div")[7]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''deselect sodium button'''
        
        button = buttonList.find_elements(By.TAG_NAME, "div")[8]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        '''select calories'''
        button = buttonList.find_element(By.TAG_NAME, "div")
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''select carbohydrates button'''
        #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[2]/label/span 
        button = buttonList.find_elements(By.TAG_NAME, "div")[1]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()
        '''select Protein button'''
        #/html/body/div/ng-view/div/print-sidebar/div/div[3]/div[1]/div/div[4]/label/span
        button = buttonList.find_elements(By.TAG_NAME, "div")[3]
        button = button.find_element(By.TAG_NAME, "label")
        button = button.find_element(By.TAG_NAME, "span")
        button.click()

    '''daily carbs'''
    dailyCarbs = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    dailyCarbList = []
    foodItems = dailyCarbs.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        dailyCarbList.append(foodList)
    secondSelectionStatus()
    # dailyCarbs = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = dailyCarbs.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            dailyCarbList[count].append(statStringList[x])
        
            
        
        count+=1
    print(dailyCarbList)
    print(); print();
    '''drinks'''
    firstSelectionStatus()
    drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[4]/div")
    drinksList = []
    foodItems = drinks.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        drinksList.append(foodList)
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = drinks.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            drinksList[count].append(statStringList[x])
        
            
        
        count+=1
    print(drinksList)
    print(); print();
    '''Salad Bar'''
    firstSelectionStatus()
    saladBar = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[5]/div")
    # saladBar = landscape.find_element(By.ID, "print-area")
    # saladBar = saladBar.find_element(By.ID, "page-1")
    # saladBar = saladBar.find_element(By.ID, "page-body")
    # saladBar = saladBar.find_element(By.ID, "print-footer")

    # saladBar = saladBar.find_elements(By.TAG_NAME, "div")[5]
    # saladBar = saladBar.find_element(By.CLASS_NAME, "footer-foodlists")
    saladBarList = [] # Ex. [ ["Lettuce", calorie, carbo, protein, totalFat, cholesterol, sodium], ....  ]
    foodItems = saladBar.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        saladBarList.append(foodList)
    secondSelectionStatus()
    # saladBar = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[5]/div")
    foodItems = saladBar.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            saladBarList[count].append(statStringList[x])
        
            
        
        count+=1
    print(saladBarList)
    print(); print();
    '''vegan and gluten-free''' # harder to process, not that important
    '''
    firstSelectionStatus()

    vegan = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[6]/div")
    veganList = []
    foodItems = vegan.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        veganList.append(foodList)
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = drinks.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems:
        tmp1 = food.find_element(By.TAG_NAME, "div")
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            veganList[count].append(statStringList[x])
        
            
        
        count+=1
    print(veganList)
    '''
    '''snack bar pastries'''
    firstSelectionStatus()
    snackPastries = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")
    snackPastriesList = []
    foodItems = snackPastries.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        snackPastriesList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = snackPastries.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            snackPastriesList[count].append(statStringList[x])
        
            
        
        count+=1
    print(snackPastriesList)
    print(); print();

    '''snack bar cookies'''
    firstSelectionStatus()
    snackCookies = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")

    snackCookiesList = []
    foodItems = snackCookies.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems[82:]:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        snackCookiesList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = snackCookies.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems[82:]:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            snackCookiesList[count].append(statStringList[x])
        
            
        
        count+=1
    print(snackCookiesList)
    print(); print();

    '''other(healthy)'''
    firstSelectionStatus()
    otherHealthy = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")

    otherHealthyList = []
    foodItems = otherHealthy.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems[119:]:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        otherHealthyList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = otherHealthy.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems[119:]:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            otherHealthyList[count].append(statStringList[x])
        
            
        
        count+=1
    print(otherHealthyList)
    print(); print();

    '''snackDesserts'''
    firstSelectionStatus()
    snackDesserts = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")

    snackDessertsList = []
    foodItems = snackDesserts.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems[132:]:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        snackDessertsList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = snackDesserts.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems[132:]:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            snackDessertsList[count].append(statStringList[x])
        
            
        
        count+=1
    print(snackDessertsList)
    print(); print();

    '''snackPies'''
    firstSelectionStatus()
    snackPies = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")

    snackPiesList = []
    foodItems = snackPies.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems[141:]:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        snackPiesList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = snackPies.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems[141:]:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            snackPiesList[count].append(statStringList[x])
        
            
        
        count+=1
    print(snackPiesList)
    print(); print();

    '''snackmisc.'''
    firstSelectionStatus()
    snackMisc = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[8]/div")

    snackMiscList = []
    foodItems = snackMisc.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = 0
    for food in foodItems[151:]:
        if count == 0:
            count +=1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        foodList = []
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        foodList.append(foodInfo[0].text) # name
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            foodList.append(statStringList[x])
        
            
        snackMiscList.append(foodList)
        count+=1
    secondSelectionStatus()
    # drinks = driver.find_element(By.XPATH, "/html/body/div/ng-view/div/div[2]/div/div/div[2]/div[3]/div")
    foodItems = snackMisc.find_elements(By.CLASS_NAME, "footer-foodlist-item")
    count = -1
    for food in foodItems[151:]:
        if count == -1:
            count += 1
            continue
        try:
            tmp1 = food.find_element(By.TAG_NAME, "div")
        except:
            break
        
        foodInfo = tmp1.find_elements(By.TAG_NAME, "span")
        
        statString = ''.join(generically_filter(foodInfo[1].text, '0123456789.,')) 
        statStringList = statString.split(",", 3)
        for x in range(3):
            snackMiscList[count].append(statStringList[x])
        
            
        
        count+=1
    print(snackMiscList)
    print(); print();






# for element in weekBlock:

#     divs = element.find_elements(By.TAG_NAME, "div")

#     day = divs[0]
#     print("April : ", day.text)

#     information = divs[1]
#     block = information.find_element(By.TAG_NAME, "div")
#     lines = block.find_elements(By.TAG_NAME, "div") 

#     for line in lines:
#         print(line.text)




#### print lower part
# others = body.find_element_by_xpath('//*[@id="print-footer"]')
# divs = others.find_elements(By.TAG_NAME, "div")
# count = 0

# for div in divs:
#     count += 1

#     if count <= 2:
#         continue
#     else:
#         block = div.find_element(By.TAG_NAME, "div")
#         title = block.find_elements(By.TAG_NAME, "span")
#         items = div.find_elements(By.CLASS_NAME, "footer-foodlist-item")

#         print("store title: {}".format(title.text))

#         for item in items:
#             name = item.find_elements(By.TAG_NAME, "div")
#             print(name.text)
    