<h1 align="center">GitHub Copilot로 Python 프로젝트 업그레이드하기</h1>
<h5 align="center">레거시 코드를 최신 안정 버전으로 복잡하게 업그레이드하기</h3>

<p align="center">
  <a href="#mega-사전-준비">사전 준비</a> •
  <a href="#books-참고-자료">참고 자료</a> •
  <a href="#학습-목표">학습 목표</a>
</p>

- **대상**: GitHub Copilot을 활용해 레거시 코드 업그레이드 시나리오를 수행하고자 하는 모든 기술자
- **학습 내용**: 프로젝트 업그레이드에 특화된 GitHub Copilot 고급 활용법을 익힙니다. 신규 개발에도 적용 가능합니다.
- **결과물**: Python 2.5 기반의 레거시 코드를 최신 Python 3 버전으로 전면 개편한 프로젝트를 완성합니다.

> [!NOTE]
> 워크샵을 찾고 계신가요? [워크샵 디렉터리](./workshop)로 이동하세요.

## 학습 목표

이 워크샵에서 여러분은 다음을 경험합니다:

  - 레거시 프로젝트를 다루기 위한 GitHub Copilot 고급 상호작용 기법 활용
  - 업그레이드 과정에서 답변을 반복적으로 검증·개선하여 프로젝트의 완성도를 높임
  - 더 나은 결과를 위한 다양한 전략과 패턴 적용
  - 업그레이드 후 프로젝트의 정확성과 완성도를 검증할 수 있는 테스트 전략 구축

## :mega: 사전 준비

워크샵 참여 전 필요한 것은 단 하나, 공개 GitHub 계정입니다. 모든 리소스와 데이터는 저장소에 포함되어 있습니다. GitHub Copilot 라이선스, 체험판 또는 무료 버전을 준비하세요.

## :books: 참고 자료

이 워크샵의 일부 내용은 아래 Microsoft Learning 모듈에서 확인할 수 있습니다(필수 아님):

- [GitHub Codespaces로 코드 작성](https://learn.microsoft.com/training/modules/code-with-github-codespaces/)
- [GitHub Copilot 고급 기능 활용](https://learn.microsoft.com/training/modules/advanced-github-copilot/)

## 주요 요점

### 1. 명확한 목표와 요구사항 정의

*무엇을 달성해야 하는가?*

최종 목표를 명확히 이해하세요. 예를 들어 레거시 프로젝트 업그레이드 시, 변경 사항의 정확성과 완성도를 검증할 수 있는 테스트 전략이 필수입니다.

*제약 조건은 무엇인가?*

예를 들어, 프로덕션 환경에서 사용하는 프로젝트라면 새로운 라이브러리나 기능 추가가 기존 코드를 깨뜨릴 수 있으므로 제한될 수 있습니다.

> [!TIP]
> 문제의 범위를 명확히 하세요. 확신이 없다면 넓게 시작해 점차 세부적으로 좁혀가세요.

### 2. 문제를 구성 요소로 분해

복잡한 문제를 작은 단위로 나누세요. 예를 들어, 핵심 컴포넌트부터 시작해 단일 API 엔드포인트나 라이브러리 함수 단위로 테스트합니다.

- 공개 함수, API 엔드포인트
- 테스트 및 테스트 환경 설정
- 구성 및 설치 과정

> [!TIP]
> 분해는 복잡성을 다루는 좋은 방법입니다. 한 번에 작은 작업에 집중할 수 있습니다.

### 3. 작업 단위(Slice) 생성

작업 단위는 전체 문제를 작은 조각으로 나눈 것입니다. 예를 들어 레거시 프로젝트 업그레이드 시, 특정 라이브러리나 함수 업그레이드에 집중할 수 있습니다.

> [!TIP]
> 작업 단위 생성 시 기능 테스트를 염두에 두세요. 간단한 테스트 스크립트나 전체 테스트 스위트가 도움이 됩니다.

### 4. 반복적 개선

처음에는 단순하게 시작하고 점진적으로 개선하세요. 매번 결과를 테스트·검증하며 올바른 방향으로 가고 있는지 확인하세요.

### 5. 예시 활용

문제 설명이나 AI 모델 프롬프트 작성 시 예시를 제공하세요. 입력과 기대 결과, 논리를 함께 설명하면 이해가 쉬워집니다.

> [!TIP]
> 예시 기반 문제 해결은 이해를 맞추는 데 효과적입니다.

### 6. 패턴 인식 및 재사용

문제에서 공통 패턴을 인식하고 기존 솔루션을 재사용하세요. 예를 들어, Python 2.5의 예외 처리 방식은 Python 3에서 오류를 유발할 수 있습니다.

> [!TIP]
> 반복적으로 유사 문제를 경험하면 패턴을 빠르게 인식할 수 있습니다.

### 7. 제약 조건 및 엣지 케이스 활용

견고한 코드를 위해 제약 조건과 엣지 케이스를 고려하세요.

### 8. 도구의 효과적 활용

GitHub Copilot, 에디터 자동완성 등 도구를 적극 활용하되, 명확한 입력과 결과 검증이 필요합니다.

> [!TIP]
> 도구에 구체적으로 지시하고 결과를 반드시 확인하세요.

### 9. 테스트 및 검증

테스트와 검증은 솔루션의 기대 동작을 보장합니다. 레거시 코드에서는 더욱 중요합니다.

> [!TIP]
> 항상 검증 단계를 포함하세요.

## :books: 참고 자료

워크샵에서 다루는 일부 기능은 아래 Microsoft Learning 모듈에서 확인할 수 있습니다(필수 아님):

- [GitHub Codespaces로 코드 작성](https://learn.microsoft.com/training/modules/code-with-github-codespaces/)
- [GitHub Copilot 고급 기능 활용](https://learn.microsoft.com/training/modules/advanced-github-copilot/)

## 기여하기

이 프로젝트는 기여와 제안을 환영합니다. 기여 시 [Contributor License Agreement (CLA)](https://cla.opensource.microsoft.com)를 확인하세요.

프로젝트는 [Microsoft 오픈소스 행동강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다. 문의는 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 연락하세요.

## 상표

이 프로젝트에는 Microsoft 및 타사 상표 또는 로고가 포함될 수 있습니다. Microsoft 상표 사용은 [Microsoft 상표 및 브랜드 가이드라인](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)을 따라야 합니다.
