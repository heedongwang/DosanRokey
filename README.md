# Dosan Rokey

두산 로키(ROKEY) 교육 과정에서 작성한 Python, 딥러닝, 컴퓨터 비전 실습 자료를 정리한 저장소입니다.

## Repository Structure

```text
DosanRokey/
├── CV/                    # 딥러닝 및 컴퓨터 비전 Jupyter Notebook
├── KIOSK/                 # 콘솔 기반 카페 키오스크 실습
└── offfice_reeservaton/   # 콘솔 기반 회의실 예약 실습
```

## Contents

### CV

Google Colab과 Jupyter Notebook에서 진행한 딥러닝 및 컴퓨터 비전 학습 기록입니다.

- NumPy 기초와 데이터 처리
- TensorFlow/Keras 기반 딥러닝 모델 실습
- 이미지 처리 및 컴퓨터 비전 실습
- 차시별 문제 풀이와 예제 코드

### KIOSK

Python과 CSV 파일 입출력을 활용한 콘솔 카페 키오스크입니다.

- 전체 메뉴 조회
- 메뉴 주문
- 메뉴 추가 및 삭제
- 기간에 따른 시즌 메뉴 처리 연습

### Office Reservation

회의실 예약 정보를 CSV 파일로 관리하는 콘솔 프로그램입니다.

- 월간 달력 출력
- 예약 현황 조회
- 예약 생성, 수정 및 삭제
- 동일 회의실의 예약 시간 중복 확인

## Environment

- Python 3
- Jupyter Notebook 또는 Google Colab
- NumPy
- TensorFlow / Keras
- OpenCV

노트북마다 사용하는 라이브러리가 다르므로, 필요한 패키지는 각 노트북의 import 셀을 기준으로 설치합니다.

## Run

저장소를 복제합니다.

```bash
git clone https://github.com/heedongwang/DosanRokey.git
cd DosanRokey
```

키오스크 프로그램:

```bash
cd KIOSK
python Kiosk_v1.py
```

회의실 예약 프로그램:

```bash
cd offfice_reeservaton
python main.py
```

컴퓨터 비전 및 딥러닝 실습은 `CV` 폴더의 `.ipynb` 파일을 Jupyter Notebook이나 Google Colab에서 실행합니다.

## Notes

- 일부 실습은 별도의 CSV 파일이나 Google Drive 데이터가 필요할 수 있습니다.
- 초기 학습 자료에는 한글 인코딩이 정상적으로 표시되지 않는 파일이 포함되어 있을 수 있습니다.
- 폴더명 `offfice_reeservaton`은 기존 실습 경로와의 호환을 위해 그대로 유지합니다.
