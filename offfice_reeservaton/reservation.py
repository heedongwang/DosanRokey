from datetime import datetime
from  reserve_data import reserveData,load_Data,save_Data

#예약할 정보 받아옵니다
#이후 사용자ID와 비밀 번호 로그인 하는 기능 추가할 예정입니다.

def input_infrom():
    room=input(f'회의실 번호를 입력하세요(현재 1번 회의실만 사용 가능합니다):')
    user= input("사용자 ID를 입력하세요: ")
    start_time = input("시작 시간을 입력하세요 (YYYY-MM-DD HH:MM): ")
    end_time = input("종료 시간을 입력하세요 (YYYY-MM-DD HH:MM): ")
    
    return room, user, start_time, end_time

#예약현황 출력
def view_reserve():
    reserve=load_Data()
    print("예약 현황:")
    for re in reserve:
        print(f"회의실 번호: {re.room} / 사용자: {re.user} / 예약시간: {re.start}~{re.end}")
    print(" ")


#예약 하기
#오늘을 기준으로 이전 날짜의 예약을 하지 못하게 추가할 예정입니다.
def make_reserve():
    print("새로운 예약을 시작합니다")
    room, user, start, end=input_infrom()
    
    new_reserve= reserveData(room,user,start,end)
    reservations=load_Data()
    
    for re in reservations:
        if re.room== room and not (new_reserve.end<= re.start or new_reserve.start >= re.end):
            print("해당 시간에는 이미 예약이 있습니다")
            print("다른 시간을 선택해 주세요")
            return
    
    reservations.append(new_reserve)
    save_Data(reservations)
    print("예약이 완료 되었습니다")


#기존 예약을 수정합니다
def change_reserve():
    print("기존 예약을 수정합니다")
    change_user=input("수정할 예약의 사용자를 입력하세요: ")
    reservations=load_Data()
    
    for re in reservations:
        if re.user==change_user:
            start=input("새로운 시작 시간을 입력하세요 (YYYY-MM-DD HH:MM): ")
            end=input("새로운 종료 시간을 입력하세요 (YYYY-MM-DD HH:MM): ")
        
            #변경된 데이터를 넘겨줍니다
            change_reserve=reserveData(re.room,change_user,start,end)
            
            #변경한 시간이 기존 예약시간과 중복되는지 확인
            for r in reservations:
                if r.room == re.room and r != re and not (change_reserve.end <= r.start or change_reserve.start >= r.end):
                    print("해당 시간에 이미 예약이 있습니다.")
                    return
        
            #기존데이터를 변경된 값으로 바꿔주고 csv에 저장합니다    
            re.start = start
            re.end = end
            save_Data(reservations)
            print("예약이 수정되었습니다.")
            return


#예약을 삭제합니다
#현재 이름이 같으면 삭제되는 과정이지만
#동일인이 여러 예약을 할 경우를 추후 추가할 예정입니다.
def delete_reserve():
    user = input("취소할 예약의 사용자를 입력하세요: ")
    reservations = load_Data()
    for re in reservations:
        if re.user == user:
            reservations.remove(re)
            save_Data(reservations)
            print("예약이 취소되었습니다.")
            return