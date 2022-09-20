## KT 공모전

### 1. 전체 실행 프로세스
```python
   # 변수 제거
    del_cols = ['ADID', 'DSP ID', '매체 ID', '애드유닛 ID', '노출 ID', 'SSP 입찰ID', 'DSP 입찰ID', 'AX 낙찰ID',
                'WUID (웹 유저 ID)', '광고 응답 광고주 도메인', '국가코드 ID', 'OS 버전 ID', '플랫폼', 'OS 종류', 'P5']
    x = x.drop(del_cols, axis=1)

    # '광고 응답 소재 카테고리' 열 관련
    # 결측치 채우기( IAB24 : Uncategorized)
    x['광고 응답 소재 카테고리'].fillna('IAB24', inplace=True)
    # 열 변환 
    x['광고 응답 소재 카테고리'] = x['광고 응답 소재 카테고리'].str[:5]
    # 특수문자 제거
    x.loc[x['광고 응답 소재 카테고리'].str[-1]=='-', '광고 응답 소재 카테고리'] = x['광고 응답 소재 카테고리'].str[:-1]
    x.loc[x['광고 응답 소재 카테고리'].str[-1]=='%', '광고 응답 소재 카테고리'] = x['광고 응답 소재 카테고리'].str[:-1]
    
    # 결측치 제거
    x.dropna(axis=1, inplace=True)
  
    # 열 변환 ( P1 ~ P4 = P1 ~ P4 / 환율 )
    x['P1'] = x['P1'] / x['환율']
    x['P2'] = x['P2'] / x['환율']
    x['P3'] = x['P3'] / x['환율']
    x['P4'] = x['P4'] / x['환율']

    # P1-P4 열 추가
    x['P1-P4'] = (x['P1'] - x['P4']) / x['P1'] * 100
    
    # '시각' 열 날짜형으로 변환
    x['시각'] = pd.to_datetime(x['시각'], format='%Y%m%d%H%M%S')

    # '시간대' 열 추가 : '시각' 열에서 시간만 추출
    x['시간대'] = x['시각'].dt.hour

    # 3시간 단위로 나누기(이상, 미만)
    for i in range(0, 24, 3):
        x.loc[x['시간대'].between(i, i+3, inclusive='left'), '시간대'] = i
    
    # 변수 제거
    x.drop(['시각'], axis=1, inplace=True)

    # 인덱스 초기화
    x.reset_index(drop=True, inplace=True)

    return x

# 데이터 전처리 함수 만들기2
def df_prep2(x):
    # 가변수화
    dumm_cols = ['ADID 타입', '사이즈 ID', '광고 응답 소재 카테고리']  
    x = pd.get_dummies(x, columns=dumm_cols, drop_first=True)

    # 정규화
    x = (x - x.min()) / (x.max() - x.min())

    return x
```


### 2. 코드 실행방법
 

### 3. 개발환경(OS)및 라이브러리
 *개발환경(OS) : 아나콘다, 구글 코랩
 *라이브러리 : scikit-learn, lightgmb
