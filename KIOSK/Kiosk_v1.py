#마지막 파일 저장 날짜 표시/ 개발자 표시
import os,sys,csv,datetime

menu={}

#메뉴 주문
def order():
    try:
        with open('menulist.csv','r',encoding='euc-kr') as of:
            lines = csv.DictReader(of)
            for row in lines:
                category = row['category']
                menu = row['menu']
                price = int(row['price'])
                
                if category not in menu:
                    menu[category] = {}

                menu[category][menu] = price  
        #csv에서 메뉴 읽어와 출력  
        print("=====================") 
        print('        MENU        ')
        print("=====================")
        for drink,price in menu.items():
            print(f'{drink}:{price}')
        print("=====================")
        
        #메뉴 선택1
        orderMenu=input("원하시는 메뉴를 입력하세요\n") 
        if orderMenu in menu:
            print(f"{orderMenu}를 선택하셨습니다")
            print(f'가격은 {menu[orderMenu]} 입니다.')
        else:
            print("메뉴에 없는 음료입니다")   
    except FileNotFoundError:
        print('메뉴 파일을 찾을 수 없습니다')
   
# 전체 메뉴 출력
def showMenu():
    try: 
        with open('menulist.csv','r',encoding='euc-kr') as sf:
            print("=====================")
            print("전체 메뉴 ")
            print("=====================")
            for line in sf:
                print(line.strip())
            print("=====================")
    except FileNotFoundError: #파일이 없으면 기본 메뉴 출력
        return {'아메리카노': 3200, '카페라떼': 4200, '바닐라 라떼': 4500}
    
#메뉴 추가   
def addMenu():
    print("=====================")
    print("메뉴를 추가합니다")
    print("=====================")
    
    newMenu=input("추가할 메뉴를 입력하세요:")
    newPrice=int(input("추가 메뉴의 가격을 입력하세요:"))
    menu[newMenu]=newPrice
    
    with open('menulist.csv','a',encoding='euc-kr') as af:
        af.write(f"{newMenu}:{newPrice}원\n")
        
    showMenu()    

    print(f"\'{newMenu}\'가 추가되었습니다.") 
    
     
 #07.29~08.10 시즌메뉴 출시   
def seansonMenu():
    args = sys.argv[:]
    filePath = args[0].split('/')
    today = datetime.now()
    print(today)
    if datetime(2024, 7, 28) <=  today < datetime(2024, 8, 11):
        filePath[-1] = 'SummerMenu.csv'
    else :
        filePath[-1] = 'Menu.csv'
    
    strFilePath = '/'.join(filePath)
    
    
#메뉴 삭제
def delMenu():  
    showMenu()
    
    delmenu=input("삭제할 메뉴를 입력하세요:")
   
    if delmenu in menu:
        del menu[delmenu]
    else:
        print("메뉴에 없는 음료입니다")
    with open("menulist.csv",'r',encoding='euc-kr') as df:
        lines = df.readlines()
        keepline = [line for line in lines if delmenu not in line]
        
    with open("menulist.csv", 'w', encoding='euc-kr') as file:
        file.writelines(keepline)    
    showMenu()
    print(f"{delmenu}가 삭제되었습니다.")
    
def start():
    print("==============================")
    print("=========HELLO CAFE===========")
    print("==========WELLCOME============")
    print("==============================")   
    
def endorder():
    print("=====================")
    print("주문이 완료되었습니다")
    print("잠시만 기다려 주세요")
    print("=====================")
    return exit()



#초기화면
def main():
    
    start()
    while True:
        print('원하는 기능을 입력해주세요')
        print('1. 전체 메뉴 보기 2. 메뉴 주문  3. 메뉴 추가 4. 메뉴 삭제 5. 주문 완료')
        choice=int(input())
        if choice==1:
            showMenu()
        elif choice==2:
            order()
        elif choice==3:
            addMenu()
        elif choice==4:
            delMenu()
        elif choice==5:
            endorder()
        else:
            print("1~5번을 입력해 주세요.")


if __name__=='__main__':
    main()
