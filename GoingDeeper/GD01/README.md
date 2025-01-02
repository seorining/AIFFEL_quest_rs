# AIFFEL Campus Online Code Peer Review Templete
- 코더 : __김희찬__
- 리뷰어 : __정우철__


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 센텐스피스 토크나이저 적용, 학습 진행; 유니그램+bpe타입 
      ![image](https://github.com/user-attachments/assets/61f9f9c3-1a4f-436c-8577-30d33ce16da3)
      ![image](https://github.com/user-attachments/assets/b8ada097-5bef-4bb6-9507-4730ad77e616)
    - KoNLPy의 MeCab 기법을 활용한 토크나이징
      ![image](https://github.com/user-attachments/assets/acbdc469-72cb-4305-ae6a-f0e5c50b0efa)
      ![image](https://github.com/user-attachments/assets/f67df545-83eb-4b8e-ab2f-e0d9bb50aa39)


- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 구글의 센텐스피스 파이썬 래퍼를 불러와 두 가지 기법으로 토큰화 진행
      ![image](https://github.com/user-attachments/assets/5bf5f7b2-44a4-4863-be8c-e381dc2af378)

        
- [ ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - SentencePiece 모델의 model_type, vocab_size 등을 변경부분이 아쉽습니다!
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 초반 모델학습의 문제점 기록 및 재수행 기록
    ![image](https://github.com/user-attachments/assets/19b1a07c-1dfd-43bc-b311-6c073b814d9c)

        
- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 깔끔한 NN모델 정의 및 재사용
      ![image](https://github.com/user-attachments/assets/982472e9-fb00-44f1-818c-5b46cdb9c03b)
      ![image](https://github.com/user-attachments/assets/ff9046e6-5c9d-4eed-a39f-2dd9d015df7a)



# 회고(참고 링크 및 코드 개선)
```
학습 시간에 오류 이야기를 자주 공유해 주시더니 프로잭트는 잘 수행된 것 같아 다행입니다!
깔끔한 코드도 상대적으로 보기가 좋네요. 이번 프로젝트도 고생 많으셨습니다!
```
