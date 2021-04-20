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

|                **URL**                | **Method** |                           **Data**                           |       **설명**       |
| :-----------------------------------: | :--------: | :----------------------------------------------------------: | :------------------: |
|               api/book/               |    POST    | {<br/>title : 소설 제목<br/>cover : 커버 이미지<br/>author : 작가<br/>} |      소설 생성       |
|          api/book/?author=?           |    GET     |                                                              | 소설 리스트 가져오기 |
|         api/book/\<int:pk\>/          |    GET     |                                                              |  소설 정보 가져오기  |
|             api/chapter/              |    POST    | {<br/>title : 챕터 제목<br/>content : 챕터 내용<br/>author : 작가<br/>book : 소설<br/>} |      챕터 생성       |
|          api/chapter/?book=?          |    GET     |                                                              | 챕터 리스트 가져오기 |
|      api/chapter/\<int:index\>/       |    GET     |                                                              |  챕터 정보 가져오기  |
|         api/chapter-comment/          |    POST    | {<br/>author : 댓글 작성 회원<br/>book : 소설<br/>chapter : 챕터<br/>context : 댓글내용<br/>parent_comment : 대댓글<br/>} |  챕터 댓글 작성하기  |
| api/chapter-comment/?book=?&chapter=? |    GET     |                                                              |  챕터 댓글 가져오기  |
|              api/review/              |    POST    | {<br/>author : 리뷰 작성 회원<br/>book : 소설<br/>title : 리뷰 제목<br/>context : 리뷰 내용<br/>review_point : 리뷰 점수<br/>} |    리뷰 작성하기     |
|      api/review/?author=?&book=?      |    GET     |                                                              | 리뷰 리스트 가져오기 |
|        api/review/\<int:pk\>/         |    GET     |                                                              |  리뷰 정보 가져오기  |
|          api/review-comment/          |    POST    | {<br/>author : 댓글 작성 회원<br/>review : 리뷰<br/>context : 댓글내용<br/>parent_comment : 대댓글<br/>} |  리뷰 댓글 작성하기  |
| api/review-comment/?book=?&chapter=?  |    GET     |                                                              |  리뷰 댓글 가져오기  |

