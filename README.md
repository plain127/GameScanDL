# GameScanDL

## Project

![gameshot](https://github.com/user-attachments/assets/0cd2268c-36a9-40f0-ae28-bf590ce66b3b)

- CNN기반 게임 스크린 샷을 넣으면 어떤 게임인지 구별해주는 식별기

## Purpose
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

### Product
- 이 중 AI가 스크린 샷으로 어떤 게임인지 구별하는 기능 제작

## Dataset
- 넥슨 게임 2024년 7월 기준 피시방 점유율 상위 12가지 
- 무작위 게임플레이 영상 수집
- 이미지 종류당 최저943장 ~ 최대2245장

## Model
### VGG16
### Pre-Trained Model
[Pretrained](https://drive.google.com/file/d/1Pzn0DTHbficggTykcDGUOAtCZaYYZ8cm/view?usp=drive_link)
