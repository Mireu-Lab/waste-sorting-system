# Set.json 설정 방법

Set.json파일에 들어가면 아래와 같습니다

```json
{
    "admin" : {
        "user" : "test",
        "password" : 1234
    },
    
    "device" : {
        "id" : 1,
        "local" : "test",
        "version" : 1
    }
}
```

| admin    |                      |
| -------- | -------------------- |
| user     | 사용자 ID            |
| password | 사용자 계정 패스워드 |

| device    |      |
| -------- | ---- |
| id     | 수거함 ID |
| local | 수거함 설치 지역 |
| version | 수거함 소프트웨어 버전 |