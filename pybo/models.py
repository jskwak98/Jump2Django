from django.db import models

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField() # 내용
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Foreign Key 선언, 질문 삭제시 Cascading하게 삭제됨
    content = models.TextField()  # 답변 내용
    create_date = models.DateTimeField()  # 답변 작성 시각
