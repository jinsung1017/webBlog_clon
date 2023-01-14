from django.core.exceptions import ValidationError  # 유효성 검증에 실패했을 떄


def validate_symbols(value):
    if ("@" in value) or ("#" in value) or ('&' in value):
        raise ValidationError('"@"와 "#" "&" 은 입력 할 수 없습니다.', code="symbol-err")  # code -> 에러코드 임의로 부여
