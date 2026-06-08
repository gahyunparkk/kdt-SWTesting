# 테스트 케이스 결과 보고서

이 파일은 SLAS(Speed Limit Assist System) 실습 요구사항에 대한 테스트 케이스 명세서이다.

## 테스트 케이스

| No. | TC ID | SRS ID | Purpose | Pre-condition | Test Procedure | Input | Expected Result | Remarks | Actual Result | Result | Severity | Priority |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SLAS-A-TC-001 | SLAS-SRS-001 | 유효 제한속도 정보 표시 확인 | 기본 조건 | 현재 Step 실행 후 기본 제한속도 정보와 보조 표시를 확인한다. | mode=WARNING, vehicleSpeed=70, cameraLimit=80, navLimit=80, offset=0 | 적용 제한속도 80, 기본 제한속도 80, 보조 표시 색상 GREEN, 과속 경고 OFF | | | Not Tested | | |
| 2 | SLAS-A-TC-002 | SLAS-SRS-002 | 제한속도 정보 없음 확인 | 기본 조건 | 현재 Step 실행 후 기본 제한속도 정보와 보조 표시를 확인한다. | cameraLimit=0, navLimit=0 | 적용 제한속도 0, 기본 제한속도 ---, 보조 표시 색상 GREEN | | | Not Tested | | |
| 3 | SLAS-A-TC-003 | SLAS-SRS-003 | OFF 모드 보조 표시 색상 확인 | 기본 조건 | 현재 Step 실행 후 보조 표시 색상을 확인한다. | mode=OFF | 적용 제한속도 80, 보조 표시 색상 OFF | | | Not Tested | | |
| 4 | SLAS-A-TC-004 | SLAS-SRS-004 | OFF 모드 경고 및 안내 출력 제한 확인 | 기본 조건 | 현재 Step 실행 후 과속 경고 및 설정속도 변경 안내를 확인한다. | mode=OFF, vehicleSpeed=90 | 적용 제한속도 80, 과속 경고 OFF, 설정속도 변경 안내 NONE | | | Not Tested | | |
| 5 | SLAS-A-TC-005 | SLAS-SRS-005 | 경고 임계값 이하 과속 경고 미출력 확인 | 기본 조건 | 차량 속도가 경고 임계값 이하일 때 과속 경고를 확인한다. | vehicleSpeed=80 | 적용 제한속도 80, 과속 경고 OFF, 보조 표시 색상 AMBER | | | Not Tested | | |
| 6 | SLAS-A-TC-006 | SLAS-SRS-006 | 경고 임계값 초과 시 과속 경고 출력 확인 | 기본 조건 | 차량 속도가 경고 임계값을 초과할 때 과속 경고를 확인한다. | vehicleSpeed=81 | 적용 제한속도 80, 과속 경고 ON, 보조 표시 색상 RED | | | Not Tested | | |
| 7 | SLAS-A-TC-007 | SLAS-SRS-007 | 경고 임계값 90% 미만 GREEN 표시 확인 | 기본 조건 | 차량 속도가 임계값 90% 미만일 때 색상을 확인한다. | vehicleSpeed=71 | 적용 제한속도 80, 보조 표시 색상 GREEN, 과속 경고 OFF | | | Not Tested | | |
| 8 | SLAS-A-TC-008 | SLAS-SRS-008 | 경고 임계값 90% 이상~이하 AMBER 표시 확인 | 기본 조건 | 차량 속도가 임계값 90% 이상 임계값 이하일 때 색상을 확인한다. | vehicleSpeed=72 | 적용 제한속도 80, 보조 표시 색상 AMBER, 과속 경고 OFF | | | Not Tested | | |
| 9 | SLAS-A-TC-009 | SLAS-SRS-009 | 경고 임계값 초과 시 RED 표시 확인 | 기본 조건 | 차량 속도가 경고 임계값을 초과할 때 색상을 확인한다. | vehicleSpeed=81 | 적용 제한속도 80, 보조 표시 색상 RED, 과속 경고 ON | | | Not Tested | | |
| 10 | SLAS-A-TC-010 | SLAS-SRS-010 | ASSIST 모드 설정속도 UP 안내 확인 | 기본 조건 | 설정속도가 적용 제한속도보다 낮을 때 안내를 확인한다. | mode=ASSIST, accSpeed=50 | 적용 제한속도 80, 설정속도 변경 안내 UP | | | Not Tested | | |
| 11 | SLAS-A-TC-011 | SLAS-SRS-011 | ASSIST 모드 설정속도 DOWN 안내 확인 | 기본 조건 | 설정속도가 적용 제한속도보다 높을 때 안내를 확인한다. | mode=ASSIST, accSpeed=100 | 적용 제한속도 80, 설정속도 변경 안내 DOWN | | | Not Tested | | |
| 12 | SLAS-A-TC-012 | SLAS-SRS-012 | WARNING 모드 설정속도 안내 미출력 확인 | 기본 조건 | WARNING 모드에서 설정속도 변경 안내 미출력을 확인한다. | mode=WARNING, accSpeed=50 | 적용 제한속도 80, 설정속도 변경 안내 NONE | | | Not Tested | | |
| 13 | SLAS-A-TC-013 | SLAS-SRS-013 | 차량 속도 입력 유효 범위 확인 | 기본 조건 | 차량 속도가 유효 범위(0~250) 내 정수일 때 정상 동작을 확인한다. | vehicleSpeed=250 | 적용 제한속도 80, 기능 제한 메시지 NONE, 시스템 상태 NORMAL | | | Not Tested | | |
| 14 | SLAS-A-TC-014 | SLAS-SRS-014 | 제한속도 입력 유효 범위 확인 | 기본 조건 | 제한속도가 유효 범위(30~130) 내 정수일 때 정상 동작을 확인한다. | cameraLimit=130, navLimit=130 | 적용 제한속도 130, 기본 제한속도 130, 기능 제한 메시지 NONE | | | Not Tested | | |
| 15 | SLAS-A-TC-015 | SLAS-SRS-015 | 속도 보정값 Offset 유효 범위 확인 | 기본 조건 | Offset이 유효 범위(-10~10) 내 정수일 때 정상 동작을 확인한다. | offset=10 | 적용 제한속도 80, 기능 제한 메시지 NONE (임계값 90 적용) | | | Not Tested | | |
| 16 | SLAS-A-TC-016 | SLAS-SRS-016 | 현재 ACC 설정속도 입력 유효 범위 확인 | 기본 조건 | ACC 설정속도가 유효 범위 내 정수일 때 정상 동작을 확인한다. | mode=ASSIST, accSpeed=130 | 적용 제한속도 80, 기능 제한 메시지 NONE, 설정속도 변경 안내 DOWN | | | Not Tested | | |
| 17 | SLAS-A-TC-017 | SLAS-SRS-017 | 입력값 유효 범위 초과 시 입력 오류 처리 확인 | 기본 조건 | 입력값이 유효 범위를 벗어날 때 시스템의 오류 처리를 확인한다. | vehicleSpeed=251 | 적용 제한속도 무효(N/A), 기능 제한 메시지 INVALID_INPUT, 과속 경고 OFF, 설정속도 변경 안내 NONE | | | Not Tested | | |
| 18 | SLAS-A-TC-018 | SLAS-SRS-018 | 시동 후 15초 미만 초기화 상태 확인 | 기본 조건 | 입력값이 유효하고 시동 후 15초 미만일 때 초기화 출력을 확인한다. | time=14 | 적용 제한속도 80, 기능 제한 메시지 INITIALIZING, 보조 표시 색상 GRAY | | | Not Tested | | |
