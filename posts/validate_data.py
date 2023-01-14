# 1. 모든 포스트 데이터 가져오기
# 2. 각각의 포스트 데이터 내용안에 & 체크하기
# 3. 만약 있다면 해당 "&" 삭제 처리
# 4. 데이터 저장하기

# 5. 시간정보 처리하기
from .models import Post


def validate_post():
    posts = Post.objects.all()
    for post in posts:
        if '&' in post.content:  # content에 "&" 있다면
            print(post.id, '번 글에 & 있다!!')
            post.content = post.content.replace("&", '')  # 있다면 & 기호 삭제
            post.save()
        if post.dt_modified < post.dt_created:  # 생성일 이전에 수정일이 있다면
            print(post.id, "번 글의 수정일이 생성일보다 과거")
            post.save()





