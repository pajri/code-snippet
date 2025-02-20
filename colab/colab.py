# region get current email
from google.colab import auth
from googleapiclient.discovery import build

auth.authenticate_user()

service = build('oauth2', 'v2')
user_info = service.userinfo().get().execute()
email_info = user_info.get('email')

print(f"Logged in as: {email_info}")
# endregion

# region mount drive
from google.colab import drive
drive.mount('/content/drive')
# endregion

# region load dataset path based on email
file_path = ''

match email_info:
  case '<your email here>':
    file_path = '<your file path here>';
  case _:
    raise ValueError("email does not exists")

print(f"file_path: {file_path}")
df = pd.read_csv(file_path)
# endregion