from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    day_of_birth: int
    month_of_birth: str
    year_of_birth: str
    photo: str
    email: str
    gender: str
    phone_number: int
    current_address: str
    city: str
    state: str

    @dataclass
    class UserInterests:
        subject: str
        hobby: str


user = User(first_name='Galiia', last_name='Uzbekova', day_of_birth=18, month_of_birth='February',
            year_of_birth='1994', photo='this-is-fine.png', email='galiiauzbekova@gmail.com', gender='Female',
            phone_number=8937365074,
            current_address='Moscow', city='Delhi', state='NCR')

user_interests = User.UserInterests(subject='English', hobby='Sports')
