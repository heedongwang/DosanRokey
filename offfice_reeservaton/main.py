import calendar
from datetime import datetime
from reservation import view_reserve, make_reserve, change_reserve, delete_reserve

def monthly():
    today=datetime.today()
    cal=calendar.TextCalendar()
    print(cal.formatmonth(today.year,today.month))
    
def startscreen():
    while True:
        monthly()
        
        print("\n원하는 메뉴를 선택해주세요") 
        print("1.현재 예약 현황 2. 예약하기 3. 예약 수정 4. 예약 삭제 5.프로그램 종료")  
        choice=int(input('선택: '))
        
        if choice==1:
            print("예약 현황으로 이동합니다")
            view_reserve()
        elif choice==2:
            print("예약하기로 이동합니다")
            make_reserve()
        elif choice==3:
            print("예약 수정으로 이동합니다")
            change_reserve()
        elif choice==4:
            print("예약 삭제로 이동합니다")
            delete_reserve()
        elif choice==5:
            print("회의실 예약을 종료합니다")
            exit()
            
if __name__ == "__main__":
    startscreen()
