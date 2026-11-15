# SJ 현장일지

Streamlit Community Cloud용 모바일 현장일지입니다.

## 배포

이 폴더의 `streamlit_app.py`, `requirements.txt`, `journal.html`, `README.md`를 GitHub 저장소의 맨 위에 올립니다. 폴더 자체나 ZIP은 올리지 않습니다.

Streamlit 배포 화면에서 다음 값을 사용합니다.

- Repository: `jichojeong-design/sj-field-journal`
- Branch: `main`
- Main file path: `streamlit_app.py`
- App URL: `sj-field-journal` (이미 사용 중이면 다른 이름 선택)

배포한 HTTPS 주소를 갤럭시 Chrome에서 직접 열고 설정 → 음성 점검 · 갤럭시에서 마이크 권한을 확인합니다. iframe의 마이크 정책과 Chrome 음성 서비스가 실제 기기에서 동작하는지 확인해야 하며, HTTPS만으로 성공을 보장하지 않습니다.

## Google 저장

Google Apps Script는 별도로 배포합니다. 앱의 설정에 해당 `/exec` URL과 연결 키를 직접 입력합니다. GitHub 코드에 연결 키를 넣지 않습니다. 브라우저의 전체 전송은 기존 Apps Script 프로토콜을 그대로 사용합니다.

현장 기록과 연결 설정은 브라우저에 보관됩니다. Streamlit Python 프로세스에 현장 기록이나 음성을 저장하지 않습니다. 브라우저 음성 서비스는 제공업체에서 처리할 수 있으며 오디오 파일을 앱에 보관하지 않습니다.

기존 `content://` 파일과 새 HTTPS 주소의 브라우저 저장소는 다릅니다. 새 주소로 기존 기록이 자동 복사되지는 않습니다. 기존 앱에서 전체 전송 완료를 먼저 확인하고 기존 파일·저장소를 보관하세요. Google 자료를 앱으로 불러오는 기능은 아직 없습니다.

공개 저장소에는 코드만 올리며 현장 기록, 연결 키, 개인정보 파일은 올리지 않습니다.

## 원본 수정 후 갱신

원본 프로젝트에서 `node build-streamlit.cjs`를 실행하면 최신 단일 HTML을 이 폴더의 `journal.html`로 복사합니다. Python 실행 파일과 요구사항 파일은 유지합니다.
