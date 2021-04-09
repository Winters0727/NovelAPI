# Endpoint 설명

계정 인증은 Token 방식입니다. (로그인 시에 key 값으로 반환)

### 계정 관련

|       **URL**        | **Method** |                           **Data**                           |      **설명**      |
| :------------------: | :--------: | :----------------------------------------------------------: | :----------------: |
| api/author/register/ |    POST    | {<br>username : 아이디<br/>password1 : 비밀번호1<br/>password2 : 비밀번호2<br/>email : 이메일<br/>nickname : 닉네임<br/>profile_image : 프로필 이미지<br/>} |      회원가입      |
|  api/author/login/   |    POST    |    {<br/>username : 아이디<br/>password : 비밀번호<br/>}     |       로그인       |
|  api/author/logout/  |    POST    |                                                              |      로그아웃      |
|   api/author/user/   |    GET     |                                                              | 유저 정보 가져오기 |
|                      |   UPDATE   | {<br/>nickname : 닉네임<br/>email : 이메일<br/>profile_image : 프로필 이미지<br/>} |   유저 정보 변경   |
|                      |   DELETE   |                                                              |     유저 삭제      |



### 소설 관련

|                  **URL**                   | **Method** |                           **Data**                           |       **설명**       |
| :----------------------------------------: | :--------: | :----------------------------------------------------------: | :------------------: |
|                 api/book/                  |    POST    | {<br/>title : 소설 제목<br/>cover : 커버 이미지<br/>author : 작가<br/>} |      소설 생성       |
|                                            |    GET     |                                                              | 소설 리스트 가져오기 |
|            api/book/\<int:pk\>/            |    GET     |                                                              |  소설 정보 가져오기  |
|        api/book/\<int:pk\>/chapter/        |    POST    | {<br/>title : 챕터 제목<br/>content : 챕터 내용<br/>author : 작가<br/>book : 소설<br/>} |      챕터 생성       |
|                                            |    GET     |                                                              | 챕터 리스트 가져오기 |
| api/book/\<int:pk\>/chapter/\<int:index\>/ |    GET     |                                                              |  챕터 정보 가져오기  |

