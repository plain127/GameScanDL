# GameScanDL

## 프로젝트

![gameshot](https://github.com/user-attachments/assets/0cd2268c-36a9-40f0-ae28-bf590ce66b3b)

- CNN기반 게임 스크린 샷을 넣으면 어떤 게임인지 구별해주는 식별기

## 목적
### Problem
- 게임의 문의절차는 인디게임에서 대기업까지 모두 생각보다 복잡하다.
- 문의센터에서 개발진에게 전달하는 비효율적인 방식
- 인게임내에서 오직 텍스트만 이용하여 신고가능
- 문의를 넣어도 답장을 받기까지 오랜 시간이 걸린다.

### Solution
1. 문제 상황 발생시 찍은 스크린 샷을 업로드
2. AI가 어떤 게임인지 구별
3. AI가 어떤 문제가 발생하였는지 파악
4. 맞춤형 문의를 제작하여 게임 개발진에게 전달

### 프로덕트
- 이 중 AI가 스크린 샷으로 어떤 게임인지 구별하는 기능 제작

## 데이터 셋
- 넥슨 게임 2024년 7월 기준 피시방 점유율 상위 12가지 
- 무작위 게임플레이 영상 수집
- 이미지 종류당 최저943장 ~ 최대2245장

## 모델
### VGG16
### 사용이유
- 높은 차원의 모델일수록 적은 데이터로는 학습이 제대로 되지 않을 가능성이 높음.
- 많은 파라미터 수 : 조정할 하이퍼파라미터가 많을수록 성능을 높일 경우의 수가 더 많음.
- 전이 학습에 유리 : 시시각각 업데이트되는 게임에 맞추어 모델을 업데이트 시켜야 하기 때문
### Pre-Trained Model
[Pretrained](https://drive.google.com/file/d/1Pzn0DTHbficggTykcDGUOAtCZaYYZ8cm/view?usp=drive_link)

## 학습결과
<img width="280" alt="결과" src="https://github.com/user-attachments/assets/13fb05af-fe2f-40f1-ad16-891a5f70ff62">

- Accuracy : 0.988
- epoch : 50
- loss : 0.0019
- steps : 522
