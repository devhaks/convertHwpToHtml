# 파이썬으로 HWP -> HTML 변환하기


### 개발 환경 스펙
- [python](https://www.python.org/downloads/) 3.12.4

### 파이썬 버전 확인
```
$ python3 --version
Python 3.12.4
```

### 가상 환경 생성 및 실행
디렉토리 내에 준비된 스크립트를 사용하여 가상 환경을 생성합니다.


1. 스크립트에 실행 권한을 부여
```
$ chmod +x create_venv.sh
```

2. 스크립트를 실행합니다.
```
$ ./create_venv.sh  
```

3. 가상 환경에 접속합니다. 터미널에 (myenv) 라고 표시되면 접속된 것입니다.
```
$ source myenv/bin/activate
(myenv)
```

### 패키지 설치 및 확인

- 가상 환경에 접속한 상태에서 패키지를 설치합니다.
```
(myenv) pip install -r requirements.txt
```

- 파일 변환에 필수인 hwp5html 버전을 확인합니다.
```
(myenv) hwp5html --version
hwp5html 0.1b15
```

### 파일 변환하기
- 디렉토리에 있는 test.hwp 파일을 html, css로 변환 합니다.
- {파일명}.hwp 기준으로 output_{파일명} 디렉토리에 파일이 생성됩니다.
```
(myenv) python convertHwpToHtml.py test.hwp
```

output_test 폴더에 변환된 파일이 생성됩니다.
```
(myenv) ls output_{파일명}
index.xhtml styles.css
```
