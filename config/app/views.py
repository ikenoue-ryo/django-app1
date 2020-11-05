from django.core.mail import send_mail


"""予約メール送信"""
def sendmail(request):
    send_mail('送信完了！', 'Example message', 'ikenoue.ryo@gmail.com', ['ryo.ikenoue@gmail.com'], fail_silently=False)
    return send_mail