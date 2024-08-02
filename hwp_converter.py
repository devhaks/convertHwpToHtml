import sys
import os
from hwp5.dataio import ParseError
from hwp5.errors import InvalidHwp5FileError
from hwp5.hwp5html import HTMLTransform
from hwp5.xmlmodel import Hwp5File

def convert_hwp_to_html(hwp_file, output_dir):
    try:
        # 출력 디렉토리 생성
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # HWP 파일 열기
        hwp5file = Hwp5File(hwp_file)

        # HTML 변환기 생성
        html_transform = HTMLTransform()
        
        # styles.css 파일 생성
        css_file = os.path.join(output_dir, 'styles.css')
        with open(css_file, 'wb') as f:
            html_transform.transform_hwp5_to_css(hwp5file, f)
        
        # index.xhtml 파일 생성
        xhtml_file = os.path.join(output_dir, 'index.xhtml')
        with open(xhtml_file, 'wb') as f:
            html_transform.transform_hwp5_to_xhtml(hwp5file, f)
        
        # bindata 추출 (있는 경우)
        bindata_dir = os.path.join(output_dir, 'bindata')
        html_transform.extract_bindata_dir(hwp5file, bindata_dir)
        
        print(f"변환 완료. 출력 디렉토리: {output_dir}")
        print(f"생성된 파일: styles.css, index.xhtml")
        if os.path.exists(bindata_dir):
            print("bindata 디렉토리가 생성되었습니다.")
    except ParseError as e:
        print(f"파싱 오류: {e}")
    except InvalidHwp5FileError as e:
        print(f"잘못된 HWP 파일: {e}")
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python script.py <입력_HWP_파일>")
        sys.exit(1)
    
    hwp_file = sys.argv[1]
    output_dir = 'output_' + hwp_file.split('.')[0]
    
    convert_hwp_to_html(hwp_file, output_dir)