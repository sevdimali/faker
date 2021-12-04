from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{company_suffix}} {{last_name}}{{last_name}}{{last_name}}",
        "{{company_suffix}} {{last_name}}",
        "{{last_name}}{{last_name}}",
        "{{last_name}}{{last_name}}{{last_name}}",
    )

    catch_phrase_words = (
        (
            "적응된",
            "숙련된",
            "자동화된",
            "안정적인",
            "비즈니스 중점적",
            "중심이",
            "복제된",
            "효율적인",
            "설정 가능한",
            "크로스 그룹",
            "크로스 플랫폼",
            "사용자 중심의",
            "조절 가능한",
            "디지털화된",
            "출판된",
            "다양한",
            "낮은",
            "강화된",
            "인체 공학적인",
            "특별한",
            "확장된",
            "확대된",
            "1:1",
            "최전방",
            "완벽히 설정된",
            "함수 기반의",
            "미래가 보장된",
            "관리된",
            "모니터링되는",
            "멀티 채널",
            "다중 주파수",
            "멀티 레이어",
            "조직화된",
            "객체 기반의",
            "공개 아키텍쳐",
            "오픈소스",
            "최적화된",
            "선택적",
            "유기농",
            "수익에 중점을 둔",
            "프로그래밍 가능한",
            "진보적인",
            "공개 키",
            "품질 중심의",
            "반동적인",
            "재정렬",
            "줄어든",
            "리버스 엔지니어링된",
            "올바른 사이즈의",
            "강력한",
            "원활한",
            "안전한",
            "자가 이용 가능한",
            "공유 가능한",
            "독보적인",
            "무결점의",
            "변경 가능한",
            "동기화",
            "융합력있는",
            "융합된",
            "단체 기반의",
            "총",
            "트리플 버퍼",
            "다용도",
            "더 커진",
            "업그레이드 가능한",
            "더 작아진",
            "유저 친화적",
            "가상",
            "비전 있는",
        ),
        (
            "24시간",
            "24/7",
            "3세대",
            "4세대",
            "5세대",
            "6세대",
            "작동",
            "분석중인",
            "비대칭",
            "비동기",
            "고도 기반",
            "백그라운드",
            "주파수 탐지 가능",
            "요약",
            "클라이언트 단",
            "클라이언트-서버",
            "밀착",
            "결합된",
            "합성물",
            "상황에 맞는",
            "문맥 기반",
            "컨텐츠 기반",
            "헌신적",
            "교훈적",
            "방향",
            "분리된",
            "다이나믹",
            "환경 친화적",
            "실행",
            "취약점",
            "스며든",
            "수요 중심",
            "장거리",
            "글로벌",
            "그리드 가능",
            "휴리스틱",
            "고단계",
            "분리형",
            "인간자원",
            "하이브리드",
            "선구적",
            "로컬",
            "물류",
            "최대화",
            "결정",
            "휴대형",
            "모듈형",
            "멀티미디어",
            "다중 상태",
            "멀티 태스킹",
            "국가적",
            "범국가적",
            "중립형",
            "다음 세대",
            "객체 지향적",
            "필수",
            "최적화된",
            "근본적",
            "실시간",
            "역수",
            "지역적",
            "확장",
            "보조",
            "해답 기반",
            "안정적",
            "정적",
            "가치추가",
            "웹 사용 가능",
            "잘 모듈화된",
            "무관리",
            "무해한",
            "무관용",
        ),
        (
            "능력",
            "접근",
            "어댑터",
            "알고리즘",
            "연합",
            "분석",
            "어플리케이션",
            "접근",
            "아키텍쳐",
            "아카이브",
            "인공지능",
            "배열",
            "태도",
            "벤치마크",
            "예산 관리",
            "환경",
            "생산 능력",
            "도전",
            "회로",
            "융합",
            "컨셉",
            "축적",
            "우연성",
            "코어",
            "고객 만족",
            "데이터베이스",
            "정의",
            "에뮬레이션",
            "인코딩",
            "암호화",
            "엑스트라넷",
            "펌웨어",
            "유연성",
            "예보",
            "프레임",
            "프레임워크",
            "함수",
            "그래픽 인터페이스",
            "그룹웨어",
            "GUI",
            "하드웨어",
            "안내 창구",
            "계층",
            "허브",
            "미디어 정보",
            "환경",
            "설치과정",
            "인터페이스",
            "인트라넷",
            "지식 기반",
            "LAN",
            "미들웨어",
            "마이그레이션",
            "모델",
            "관리자",
            "모니터링",
            "공개 시스템",
            "패러다임",
            "정책",
            "포탈",
            "제품",
            "프로젝트",
            "프로토콜",
            "서비스 창구",
            "소프트웨어",
            "솔루션",
            "보안구역",
            "전략",
            "구조체",
            "성공",
            "지원",
            "시너지",
            "엔진",
            "표준",
            "시간화",
            "공구",
            "웹 사이트",
        ),
    )

    bsWords = (
        (
            "다용도의",
            "통합된",
            "간소화된",
            "최적화된",
            "진화된",
            "변화된",
            "포용적인",
            "사용 가능한",
            "웅장한",
            "재평가된",
            "재발명된",
            "구조적인",
            "강화된",
            "장려하는",
            "변화무쌍한",
            "자율적인",
            "선구적인",
            "화폐화된",
            "전략적인",
            "발전하는",
            "합성",
            "배송",
            "혼합된",
            "최대화된",
            "벤치마킹된",
            "신속한",
            "깨끗한",
            "시각적인",
            "창의적인",
            "큰",
            "폭발하는",
            "확장된",
            "엔지니어",
            "혁명적인",
            "제작된",
            "취약점의",
            "배열적인",
            "문화적인",
        ),
        (
            "온라인 쇼핑",
            "가치 상승",
            "선구적",
            "철벽",
            "혁명적",
            "가변",
            "창조적",
            "직감",
            "전략적",
            "전자 비즈니스",
            "끈끈한",
            "1:1",
            "24/7",
            "글로벌",
            "B2B",
            "B2C",
            "고운",
            "가상",
            "바이러스성",
            "다이나믹",
            "24/365",
            "고사양",
            "킬러",
            "자기장",
            "최첨단",
            "닷컴",
            "섹시",
            "백 엔드",
            "실시간",
            "효율적",
            "프론트 엔드",
            "무결점",
            "확장",
            "턴키",
            "세계급",
            "오픈 소스",
            "크로스 플랫폼",
            "크로스 미디어",
            "엔터프라이즈",
            "통합",
            "강렬한",
            "무선",
            "투명",
            "다음 세대",
            "날카로운",
            "창의적",
            "반투명",
            "유비쿼터스",
            "플러그 앤 플레이",
            "융합",
            "강력한",
            "강렬한",
            "부자",
        ),
        (
            "시너지",
            "패러다임",
            "마케팅",
            "파트너쉽",
            "인프라",
            "플랫폼",
            "채널",
            "커뮤니티",
            "솔루션",
            "전자 서비스",
            "포탈",
            "기술",
            "컨텐츠",
            "생산라인",
            "관계",
            "아키텍쳐",
            "인터페이스",
            "전자시장",
            "전자화폐",
            "시스템",
            "주파수",
            "모델",
            "어플리케이션",
            "사용자들",
            "스키마",
            "네트웍스",
            "앱",
            "매트릭스",
            "전자 비즈니스",
            "경험",
            "웹서비스",
            "방법론",
        ),
    )

    company_suffixes = ("(주)", "주식회사", "(유)", "유한회사")
