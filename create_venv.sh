#!/bin/bash

# 가상환경 이름 설정 (기본값: myenv)
VENV_NAME=${1:-myenv}

# 가상환경 생성
python3 -m venv $VENV_NAME

# 가상환경 활성화
source $VENV_NAME/bin/activate

# 가상환경 정보 출력
echo "가상환경 '$VENV_NAME'이(가) 생성되고 활성화되었습니다."
echo "현재 Python 버전:"
python --version
echo "가상환경 경로: $VIRTUAL_ENV"

# pip 업그레이드
pip install --upgrade pip

echo "pip가 최신 버전으로 업그레이드되었습니다."
echo "필요한 패키지를 설치하려면 'pip install <패키지명>'을 사용하세요."
echo "가상환경을 비활성화하려면 'deactivate' 명령어를 사용하세요."