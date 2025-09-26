# upgraded 폴더 파일 구조 설명

`upgraded` 폴더는 기존 `legacy` 폴더의 모든 파일과 디렉토리 구조를 그대로 복사한 폴더입니다.

## 최상위 파일 및 폴더
- MANIFEST.in
- README.rst
- distribute-0.6.10.tar.gz
- distribute_setup.py
- setup.py
- docs/
- guachi/
- guachi.egg-info/

## docs/
- Makefile
- build/
  - doctrees/
    - changelog.doctree
    - environment.pickle
    - example_usage.doctree
    - getting_started.doctree
    - index.doctree
    - other_uses.doctree
  - html/
    - .buildinfo
    - changelog.html
    - example_usage.html
    - genindex.html
    - getting_started.html
    - index.html
    - objects.inv
    - other_uses.html
    - search.html
    - searchindex.js
    - _sources/
      - changelog.txt
      - example_usage.txt
      - getting_started.txt
      - index.txt
      - other_uses.txt
    - _static/
      - basic.css
      - default.css
      - doctools.js
      - file.png
      - jquery.js
      - minus.png
      - plus.png
      - pygments.css
      - searchtools.js
      - sidebar.js
      - underscore.js
- source/
  - changelog.rst
  - conf.py
  - example_usage.rst
  - getting_started.rst
  - index.rst
  - other_uses.rst
  - _static/
    - default.css

## guachi/
- __init__.py
- config.py
- database.py
- tests/
  - test_configmapper.py
  - test_configurations.py
  - test_database.py
  - test_integration.py

## guachi.egg-info/
- PKG-INFO
- SOURCES.txt
- dependency_links.txt
- top_level.txt

---

이 구조는 Python 패키지와 문서, 테스트 코드, 배포 관련 파일 등으로 구성되어 있습니다. 각 디렉토리와 파일은 원본 `legacy` 폴더와 동일하게 복사됩니다.