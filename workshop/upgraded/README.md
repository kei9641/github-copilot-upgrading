# upgraded 폴더 파일 구조 설명

`upgraded` 폴더는 기존 `legacy` 폴더의 모든 파일과 디렉토리 구조를 그대로 복사한 폴더입니다.

## 최상위 파일 및 폴더 및 역할
- **MANIFEST.in**: 패키지에 포함될 파일 목록 지정
- **README.rst**: 프로젝트 설명
- **distribute-0.6.10.tar.gz**: 배포용 패키지 소스
- **distribute_setup.py**: 배포 패키지 설치 스크립트
- **setup.py**: 패키지 설치 및 배포 설정
- **docs/**: 프로젝트 문서 및 Sphinx 빌드 결과
- **guachi/**: 주요 Python 모듈 및 테스트 코드
- **guachi.egg-info/**: 패키지 메타데이터 정보

## docs/
### docs/
- **Makefile**: 문서 빌드 자동화
- **build/**: Sphinx 빌드 결과물
  - **doctrees/**: Sphinx 내부 캐시
  - **html/**: HTML 문서 및 리소스
    - **_sources/**: 원본 문서 텍스트
    - **_static/**: 정적 리소스(CSS, JS, 이미지)
- **source/**: Sphinx 문서 원본(rst, conf.py)
  - **_static/**: 커스텀 CSS

## guachi/
### guachi/
- **__init__.py**: guachi 모듈 초기화
- **config.py**: 설정 관련 기능
- **database.py**: 데이터베이스 연동 기능
- **tests/**: 테스트 코드
  - **test_configmapper.py**: 설정 매핑 테스트
  - **test_configurations.py**: 설정 기능 테스트
  - **test_database.py**: DB 기능 테스트
  - **test_integration.py**: 통합 테스트

## guachi.egg-info/
### guachi.egg-info/
- **PKG-INFO**: 패키지 정보
- **SOURCES.txt**: 소스 파일 목록
- **dependency_links.txt**: 의존성 링크
- **top_level.txt**: 최상위 패키지 목록


---

## 의존성
이 프로젝트는 Python 패키지 관리 및 테스트를 위해 아래와 같은 의존성을 사용합니다.

- **pytest**: 테스트 코드 실행을 위한 프레임워크
- (문서화용) **Sphinx**: docs 폴더 문서 빌드에 필요
- (배포용) **setuptools**: 패키지 배포에 필요

의존성은 `requirements.txt` 파일에 정의되어 있습니다. 추가적으로 필요한 패키지가 있다면 해당 파일에 추가해 주세요.

---

이 구조는 Python 패키지와 문서, 테스트 코드, 배포 관련 파일 등으로 구성되어 있습니다. 각 디렉토리와 파일은 원본 `legacy` 폴더와 동일하게 복사됩니다.