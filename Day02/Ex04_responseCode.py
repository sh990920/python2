'''
서버요청 : request
서버응답 : response

http 응답(response) 코드
    200번대 응답 : 성공(Success)
    300번대 응답 : 리다이렉션(Redirection)
    400번대 응답 : 클라이언트 에러(Cliect_Error)
        ex) 404 찾을 수 없는 페이지(주소 잘못 입력)
            403 권한 문제
    500번대 응답 : 서버 에러(Server_Error)
        ex) 503 서버가 요청을 처리할 준비가 되지 않음
            (개발자 코드 에러 발생 했을 경우)

'''
import requests

url = 'http://172.20.10.2:8888'
response = requests.get(url)
print('응답 코드 : {}'.format(response.status_code))

