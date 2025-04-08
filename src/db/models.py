from choice_enum import ChoiceEnumeration, Option
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    TextField,
)

from src.db.helpers import BaseIdModel


class Major(BaseIdModel):
    _create_table = True
    name = CharField(max_length=100, unique=True)


class User(BaseIdModel):
    _create_table = True

    class Type(ChoiceEnumeration):
        STUDENT = Option("s", "Student")
        ADMIN = Option("a", "Admin")
        OWNER = Option("o", "Owner")

    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    student_id = IntegerField(unique=True)
    phone = CharField(max_length=11)
    password = CharField(max_length=64, null=True)
    major = ForeignKeyField(Major, backref="users")
    type = CharField(max_length=1, choices=Type.CHOICES)


class Competition(BaseIdModel):
    _create_table = True
    start = DateTimeField()
    end = DateTimeField()
    score_threshold = IntegerField()


class Question(BaseIdModel):
    _create_table = True
    text = TextField()
    img = TextField()
    pdf = TextField()
    has_choices = BooleanField(default=True)
    score = IntegerField()
    compettion = ForeignKeyField(Competition, backref="questions")


class ChoiceAnswer(BaseIdModel):
    _create_table = True
    question = ForeignKeyField(Question, backref="choices")
    text = TextField()
    img = TextField()
    pdf = TextField()
    is_correct = BooleanField(default=False)


class Participant(BaseIdModel):
    _create_table = True
    user = ForeignKeyField(User)
    competition = ForeignKeyField(Competition)


class ParticipantAnswers(BaseIdModel):
    _create_table = True
    participant = ForeignKeyField(Participant)
    question = ForeignKeyField(Question)
    choice_answer = ForeignKeyField(ChoiceAnswer)
    text_answer = TextField()
    img_answer = TextField()
    pdf_answer = TextField()
    is_approved = BooleanField(default=False)
    is_correct = BooleanField(default=False)
